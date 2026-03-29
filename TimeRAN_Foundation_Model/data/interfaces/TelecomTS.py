from pathlib import Path
from typing import Dict
import numpy as np
import pandas as pd
import torch
from torch.utils.data import Dataset

class TelecomTS(Dataset):
    """TelecomTS Dataset can be used for all downstream tasks: Anomaly Detection, Classification, Forecasting, Imputation"""

    def __init__(self, data: str, task: Dict, split: str, conf: Dict):

        assert split in ("train", "test")
        if "name" not in task:
            raise ValueError("task must contain key 'name'")

        self.data = Path(data)
        self.task = task
        self.split = split
        self.seq_len = conf["seq_len"]
        self.stride = conf["stride"]
        self.train_ratio = conf["train_ratio"]
        self.horizon = conf["horizon"]
        self.dtype = float
        self.seed = 77

        self.samples = []
        self.labels = []
        self.class_names = []

        if task["name"] == "classification":
            target = task["target"]
            self._prepare_classification(target)

        elif task["name"] == "anomaly_detection":
            self._prepare_anomaly_detection()

        elif task["name"] == "imputation":
            self._prepare_imputation()

        elif task["name"] == "forecasting":
            if self.horizon is None:
                raise ValueError("conf['horizon'] must be provided for forecasting task.")
            self._prepare_forecasting()

        else:
            raise NotImplementedError(f"Task '{task['name']}' not implemented.")

    def _prepare_classification(self, target: str):
        assert target in ("anomaly", "congestion", "mobility", "services", "zones")

        target_dir = self.data / "classification_data" / target
        if not target_dir.is_dir():
            raise FileNotFoundError(f"Classification target directory not found: {target_dir}")

        files = sorted(target_dir.glob("*.csv"))
        if not files:
            raise RuntimeError(f"No CSV files found in {target_dir}")

        rng = np.random.RandomState(self.seed)
        windows_by_label = {}

        for p in files:
            df = pd.read_csv(p)

            if "label" not in df.columns:
                raise RuntimeError(f"Missing 'label' column in {p.name}")

            x_df = df.drop(columns=["label"])
            x_df = x_df.select_dtypes(include=[np.number])
            x_full = x_df.to_numpy(dtype=np.float32)

            if target == "anomaly":
                y_full = df["label"].to_numpy()
            else:
                y_file = int(df["label"].iloc[0])

            T = x_full.shape[0]
            max_start = T - self.seq_len
            if max_start < 0:
                continue

            for start in range(0, max_start + 1, self.stride):
                x_win = x_full[start:start + self.seq_len].T

                if target == "anomaly":
                    y_win = y_full[start:start + self.seq_len]
                    y = int((y_win == 1).any())   
                else:
                    y = y_file

                windows_by_label.setdefault(y, []).append(x_win)

        if not windows_by_label:
            raise RuntimeError("No windows created. Check seq_len, stride, and data sizes.")

        label_keys = sorted(windows_by_label.keys())
        self.class_names = [str(k) for k in label_keys]
        label_to_idx = {k: i for i, k in enumerate(label_keys)}

        counts = {k: len(windows_by_label[k]) for k in label_keys}
        min_count = min(counts.values())
        if min_count == 0:
            raise RuntimeError(f"One class has 0 windows. Counts: {counts}")

        for k in label_keys:
            rng.shuffle(windows_by_label[k])
            windows_by_label[k] = windows_by_label[k][:min_count]

        n_train = int(self.train_ratio * min_count)

        self.samples = []
        self.labels = []

        for k in label_keys:
            wins = windows_by_label[k]
            use = wins[:n_train] if self.split == "train" else wins[n_train:]
            self.samples.extend(use)
            self.labels.extend([label_to_idx[k]] * len(use))

        perm = rng.permutation(len(self.samples))
        self.samples = [self.samples[i] for i in perm]
        self.labels = [self.labels[i] for i in perm]

        if not self.samples:
            raise RuntimeError("No windows created. Check seq_len, stride, and data sizes.")

    def _prepare_anomaly_detection(self):
        base = self.data / "anomaly_detection_data" / self.split
        if not base.is_dir():
            raise FileNotFoundError(f"Anomaly detection directory not found: {base}")

        paths = sorted(base.glob("*.csv"))
        if not paths:
            raise RuntimeError(f"No CSV files found under: {base}")

        if self.split == "test":
            p = np.random.choice(paths)
            print(f"[TelecomTS anomaly_detection] Selected test file: {p.name}")
            paths = [p]

        for p in paths:
            df = pd.read_csv(p).select_dtypes(include=[np.number])
            if df.empty:
                continue

            values = df.to_numpy(dtype=np.float32)
            T = values.shape[0]
            if T < self.seq_len:
                continue

            if self.split == "train":
                ts = values.astype(np.float32)
                y_full = np.zeros(T, dtype=np.int64)
            else:
                if values.shape[1] < 2:
                    continue
                ts = values[:, :-1].astype(np.float32)
                y_full = values[:, -1].astype(np.int64)

            T2 = ts.shape[0]
            if T2 < self.seq_len:
                continue

            max_start = T2 - self.seq_len
            for start in range(0, max_start + 1, self.stride):
                x_win = ts[start:start + self.seq_len].T
                y_win = y_full[start:start + self.seq_len].astype(np.int64)
                self.samples.append(x_win)
                self.labels.append(y_win)

        if not self.samples:
            raise RuntimeError("No windows created for anomaly_detection. Check seq_len/stride and file lengths.")

        self.class_names = ["pointwise_anomaly"]

    def _prepare_imputation(self):
        target_dir = self.data / "imputation_forecasting_data"
        if not target_dir.is_dir():
            raise FileNotFoundError(f"Imputation/forecasting directory not found: {target_dir}")

        paths = sorted(target_dir.glob("data_*.csv"))
        if not paths:
            raise RuntimeError(f"No data_*.csv files found in {target_dir}")

        min_required = self.seq_len

        for p in paths:
            df = pd.read_csv(p)

            to_drop = [c for c in ["timestamp", "UL_Protocol", "DL_Protocol"] if c in df.columns]
            df = df.drop(columns=to_drop, errors="ignore")
            df = df.select_dtypes(include=[np.number])

            if df.empty:
                continue

            arr = df.to_numpy(dtype=np.float32)
            T = arr.shape[0]
            if T < min_required:
                continue

            split_idx = int(self.train_ratio * T)
            ts = arr[:split_idx] if self.split == "train" else arr[split_idx:]

            T_split = ts.shape[0]
            if T_split < min_required:
                continue

            max_start = T_split - min_required
            if max_start < 0:
                continue

            for start in range(0, max_start + 1, self.stride):
                x_win = ts[start:start + self.seq_len]
                x_win = x_win.T
                self.samples.append(x_win)

        if not self.samples:
            raise RuntimeError(f"No windows created for imputation. Check seq_len={self.seq_len}, stride={self.stride}, and data.")

    def _prepare_forecasting(self):
        target_dir = self.data / "imputation_forecasting_data"
        if not target_dir.is_dir():
            raise FileNotFoundError(f"Imputation/forecasting directory not found: {target_dir}")

        paths = sorted(target_dir.glob("data_*.csv"))
        if not paths:
            raise RuntimeError(f"No data_*.csv files found in {target_dir}")

        if self.horizon is None:
            raise ValueError("horizon must be set for forecasting task.")

        min_required = self.seq_len + self.horizon

        for p in paths:
            df = pd.read_csv(p)

            to_drop = [c for c in ["timestamp", "UL_Protocol", "DL_Protocol"] if c in df.columns]
            df = df.drop(columns=to_drop, errors="ignore")
            df = df.select_dtypes(include=[np.number])

            if df.empty:
                continue

            arr = df.to_numpy(dtype=np.float32)
            T = arr.shape[0]
            if T < min_required:
                continue

            split_idx = int(self.train_ratio * T)
            ts = arr[:split_idx] if self.split == "train" else arr[split_idx:]

            T_split = ts.shape[0]
            if T_split < min_required:
                continue

            max_start = T_split - min_required
            if max_start < 0:
                continue

            for start in range(0, max_start + 1, self.stride):
                x_win = ts[start:start + self.seq_len]
                y_win = ts[start + self.seq_len:start + self.seq_len + self.horizon]

                x_win = x_win.T
                y_win = y_win.T

                self.samples.append(x_win)
                self.labels.append(y_win)

        if not self.samples:
            raise RuntimeError(f"No windows created for forecasting. Check seq_len={self.seq_len}, horizon={self.horizon}, stride={self.stride}, and data.")

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx: int):
        x = self.samples[idx]
        x = torch.as_tensor(x, dtype=self.dtype)

        input_mask = torch.ones(self.seq_len, dtype=self.dtype)

        if self.task["name"] == "classification":
            y = self.labels[idx]
            return x, input_mask, y

        if self.task["name"] == "anomaly_detection":
            y = self.labels[idx]
            y = torch.as_tensor(y, dtype=torch.long)
            return x, input_mask, y

        if self.task["name"] == "imputation":
            return x, input_mask

        if self.task["name"] == "forecasting":
            y = self.labels[idx]
            y = torch.as_tensor(y, dtype=self.dtype)
            return x, input_mask, y

        raise NotImplementedError(f"__getitem__ not implemented for task {self.task}")
