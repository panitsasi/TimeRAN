# TimeRAN Model Usage

This directory provides task-specific implementations of **TimeRAN** across multiple downstream analytics tasks, including:
- anomaly detection
- classification
- forecasting
- imputation

We include the **TelecomTS** dataset as a representative dataset covering all supported tasks. Additional datasets can be integrated with minimal modifications.

> ⚠️ **Note:** The results presented in the notebooks are intended as proof-of-concept demonstrations and are not fully optimized; improved performance may be achieved through careful configuration tuning and hyperparameter optimization.

---

## 📊 Supported Tasks

Each task is organized in its own folder:

```
anomaly_detection/
classification/
forecasting/
imputation/
```

Each folder contains:
- a `config.yaml` file (experiment configuration)
- a Jupyter notebook for running the task

---

## 🚀 Running Experiments

To run a task, navigate to the corresponding folder and open the notebook:

### Example: Classification

```
cd classification
jupyter notebook classification.ipynb
```

---

## ⚙️ Configuration Overview

All experiments are controlled via the `config.yaml` file.

### 🔧 Core Model Parameters

```
backend: TimeRAN        # Model backbone
variant: base           # small | base | large
mode: full_finetuning   # full_finetuning | linear_probing
lora: false             # Enable LoRA (used only with full_finetuning)

batch_size: 32          # Training batch size
epochs: 5               # Number of training epochs

init_lr: 1e-5           # Initial learning rate (used for fine-tuning)
max_lr: 1e-4            # Maximum learning rate (scheduler peak, for fine-tuning)
max_norm: 5             # Gradient clipping norm (for stable fine-tuning)

seed: 77                # Random seed for reproducibility
device: 0               # GPU device index (e.g., 0 for cuda:0)
```

### 🧠 Training Modes

- `full_finetuning`  
  → updates all model parameters  

- `linear_probing`  
  → freezes backbone, trains only task head  

- `lora: true`  
  → enables parameter-efficient fine-tuning (only valid with `full_finetuning`)

---

## 📦 Dataset Configuration

```
dataset:
  class: TelecomTS
  data: ../data/datasets/TelecomTS
  train_ratio: 0.7

  task:
    name: anomaly_detection | classification | forecasting | imputation
    target: <task-specific>

  seq_len: 512
  stride: 512
  horizon: None
  mask_ratio: 0.3
```

---

## 🎯 Task-Specific Notes

### Anomaly Detection
- `target: None`
- Uses reconstruction-based anomaly scoring
---

### Classification

```
task:
  name: classification
  target: congestion
```

- The `target` specifies the classification task
- Available targets depend on the dataset

For **TelecomTS**, targets correspond to dataset folders such as:

```
classification_data/
├── anomaly/
├── congestion/
├── mobility/
├── services/
└── zones/
```

👉 Simply change:
```
target: congestion
```
to:
```
target: mobility
```
(or any available task)

---

### Forecasting
- Predicts future values based on historical sequences
- Controlled via `horizon`

---

### Imputation
- Reconstructs missing values
- Controlled via `mask_ratio`

---

## 🔁 Customization & Extensions

- New datasets can be integrated with minimal modifications by:
  - adding a dataset loader in `data/interfaces/`
  - updating the dataset path in `config.yaml`
  - importing and adding the datasets in the .ipynb task files

- Hyperparameters (e.g., learning rate, batch size, sequence length) can be adjusted directly in `config.yaml`

- Results can be further improved through:
  - longer training
  - different `mode` (e.g., full fine-tuning vs. linear probing)
  - hyperparameter optimization
---

## 📄 Citation

If you find **TimeRAN** useful in your research, please consider citing:

```bibtex
@article{panitsas2026timeran,
  title   = {A Family of Open Time-Series Foundation Models for the Radio Access Network},
  author  = {Panitsas, Ioannis and Tassiulas, Leandros},
  journal = {arXiv preprint arXiv:2604.04271},
  year    = {2026},
  doi     = {10.48550/arXiv.2604.04271}
}
```
