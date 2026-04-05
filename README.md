# TimeRAN

**TimeRAN** is a unified multi-task learning framework for time-series modeling in the Radio Access Network (RAN), focusing on higher-layer (L2+) RAN functions. It leverages a lightweight transformer-based time-series foundation model, adapted to RAN telemetry through large-scale pretraining on the **TimeRAN DataPile**, to learn transferable representations shared across tasks. By combining a shared backbone with a small number of task-specific heads, TimeRAN supports diverse downstream RAN tasks, including anomaly detection, classification, forecasting, and imputation, while enabling efficient generalization across heterogeneous network environments and domains.

---

## 🚀 Installation

### 1. Install Conda (if not installed)

```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
source ~/.bashrc
```

---

### 2. Clone the repository

```
git clone https://github.com/panitsasi/TimeRAN.git
cd TimeRAN
```

---

### 3. Create the Conda environment

```
conda env create -f environment.yml
conda activate TimeRAN
```

If the environment already exists:

```
conda env update -f environment.yml --prune
```

---

## 📥 Download Pretrained Checkpoints

Model checkpoints are not included in the repository due to GitHub file size limits.

### 1. Create checkpoint directories

```
mkdir -p TimeRAN_Foundation_Model/data/checkpoints/{small,base,large}
```

---

### 2. Download checkpoints

```
cd TimeRAN_Foundation_Model/data/checkpoints

gdown 1fJNCkufmfWC6zHecz10PUyreD0PhBOMJ -O base/TimeRAN_base.pth
gdown 1gz23mmP4ZiNznCloObEaSlVaJH21fyxJ -O small/TimeRAN_small.pth
gdown 1We9zE5BV6Iwkc_EKSAhP28B3wcM7RZRd -O large/TimeRAN_large.pth
```

---

## 📁 Repository Structure

```
TimeRAN/
├── environment.yml
├── TimeRAN_DataPile/
└── TimeRAN_Foundation_Model/
    ├── anomaly_detection/
    │   ├── config.yaml
    │   └── zero_shot_anomaly_detection.ipynb
    ├── classification/
    │   ├── classification.ipynb
    │   ├── config.yaml
    │   └── representation_learning.ipynb
    ├── forecasting/
    │   ├── config.yaml
    │   └── forecasting.ipynb
    ├── imputation/
    │   ├── config.yaml
    │   └── zero_shot_imputation.ipynb
    ├── data/
    │   ├── checkpoints/
    │   │   ├── base/TimeRAN_base.pth
    │   │   ├── small/TimeRAN_small.pth
    │   │   └── large/TimeRAN_large.pth
    │   ├── datasets/
    │   │   └── TelecomTS/
    │   └── interfaces/
    │       └── TelecomTS.py
    └── README.md
```

---


## 📄 Citation

If you find **TimeRAN** useful in your research, please consider citing:

```bibtex
@article{panitsas2026timeran,
  title={A Family of Open Time-Series Foundation Models for the Radio Access Network},
  author={Panitsas, Ioannis and Tassiulas, Leandros},
  journal={arXiv preprint arXiv:XXXX.XXXXX},
  year={2026}
}
```

---
