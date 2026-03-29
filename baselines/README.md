# Baselines, Architectures, and Training Details

This document summarizes the baseline models used across the downstream tasks evaluated in **TimeRAN**, including their architectures, training setup, and task-specific configurations. The baseline architectures and task coverage below are aligned with the models reported in the paper.

The implementation code for the baselines is organized under:

```text
baselines/
├── models/
│   ├── deep_learning_models/
│   └── statistical_models/
```

---

## 1. Baseline Families by Task

### Anomaly Detection
The anomaly detection baselines reported in the paper are:

- Autoformer
- Informer
- TimesNet

In addition, the paper compares against:
- TimeRAN variants
- MOMENT variants

For anomaly detection, the task is formulated over fixed input windows and evaluated using reconstruction-based anomaly scores computed as the mean reconstruction error aggregated across all channels, and reported using Adjusted F1.

---

### Classification
The classification baselines reported in the paper are:

- Informer
- TimesNet
- 1D-CNN
- LSTM

In addition, the paper compares against:
- TimeRAN variants
- MOMENT variants

These models are evaluated on downstream classification tasks such as location, mobility, anomaly, root-cause, congestion, coverage, services, and slice-type prediction, depending on the dataset. 

---

### Forecasting
The forecasting baselines reported in the paper are:

- Autoformer
- Informer
- TimesNet
- 1D-CNN
- LSTM
- ETS
- ARIMA

In addition, the paper compares against:
- TimeRAN variants
- MOMENT variants

Forecasting is evaluated for multiple prediction horizons. The horizons reported in the paper are:

- 32
- 64
- 128
- 208 

---

### Imputation
The imputation baselines reported in the paper are:

- Forward Fill
- Mean
- Nearest Neighbors
- Linear
- Rolling Mean

In addition, the paper compares against:
- TimeRAN variants
- MOMENT variants

Imputation is evaluated under different masking ratios. The masking ratios reported in the paper are:

- 10%
- 30%
- 50% 

---

## 2. Model Architecture Overview

The deep learning baselines are implemented under `models/deep_learning_models/`, while classical methods are implemented under `models/statistical_models/`.

### Transformer-Based Time-Series Baselines
The transformer-family baselines include:

- Informer
- Autoformer
- TimesNet

These models follow a sequence encoder design with a hidden dimension `d_model`, attention layers where applicable, feed-forward blocks, dropout, and task-specific heads.

A representative default configuration used across transformer baselines is:

```python
d_model = 512
n_heads = 4
e_layers = 2 or 3
d_ff = 1024
dropout = 0.1
activation = "gelu"
```

For higher-capacity variants, `d_ff` is increased proportionally relative to `d_model` when needed.

The input sequence length is denoted by `T`, while the input dimensionality is denoted by `C`:

- `T`: sequence length (window size)
- `C`: number of channels, determined by the dataset

A representative configuration template is shown below.

### Informer
```python
cfg = SimpleNamespace(
    d_model=512,
    n_heads=4,
    e_layers=3,
    d_ff=1024,
    dropout=0.1,
    factor=1,
    activation="gelu",
    seq_len=T,
    enc_in=C,
    dec_in=C,
    embed="fixed",
    freq="h"
)
```

### Autoformer
```python
cfg = SimpleNamespace(
    d_model=512,
    n_heads=4,
    e_layers=3,
    d_ff=1024,
    dropout=0.1,
    factor=1,
    activation="gelu",
    seq_len=T,
    enc_in=C,
    embed="fixed",
    freq="s",
    moving_avg=25
)
```

### TimesNet
```python
cfg = SimpleNamespace(
    seq_len=T,
    top_k=3,
    enc_in=C,
    d_model=512,
    d_ff=256,
    num_kernels=4,
    embed="fixed",
    freq="0.1s",
    dropout=0.1,
    e_layers=2
)
```

---

### Deep Learning Sequential Baselines
The sequential deep learning baselines include:

- 1D-CNN
- LSTM

These models operate directly on the multivariate sequence and use lightweight heads for the downstream task.

### 1D-CNN
```python
cfg = SimpleNamespace(
    seq_len=T,
    enc_in=C,
    d_model=512,
    e_layers=3,
    cnn_channels=64,
    kernel_size=5,
    stride=8,
    dilation_base=2,
    dropout=0.1,
    use_bn=True
)
```


### LSTM
```python
cfg = SimpleNamespace(
    seq_len=T,
    enc_in=C,
    d_model=512,
    e_layers=2,
    dropout=0.1,
    bidirectional=True
)
```

---

### Statistical Baselines
The statistical baselines are implemented under `models/statistical_models/` and include:

#### Forecasting
- ETS
- ARIMA

#### Imputation
- Forward Fill
- Mean
- Linear
- Rolling Mean

These methods do not rely on gradient-based training and are evaluated directly.

---

## 3. Shared Training Setup for Deep Learning Baselines

Unless otherwise noted, the deep learning baselines are trained in a full fine-tuning setting.

### Optimizer
The deep learning baselines are trained using Adam with weight decay:

```python
optimizer = optim.Adam(
    list(model.parameters()) + list(head.parameters()),
    lr=0.001,
    weight_decay=0.0001
)
```

### Learning Rate
Typical learning-rate settings used across tasks are:

- `init_lr`: `1e-5`
- `max_lr`: `1e-4`

These values are used as reference settings for fine-tuning-based experiments.

### Batch Size
Batch size is selected depending on the input length, dataset size, and GPU memory budget. In practice, a batch size in the range below is used:

- `batch_size`: 4 to 32

Smaller batch sizes are preferred for longer sequences or memory-intensive models.

### Number of Epochs
A small training budget is used for most experiments:

- `epochs`: 1 to 10

### Early Stopping / Limited Tuning
Hyperparameter search is intentionally limited. Tuning is stopped early when validation performance does not improve further, so the baselines should be interpreted as strong but non-exhaustively optimized reference implementations rather than fully tuned upper bounds.


### Gradient Clipping
For stability, gradient clipping is applied when needed:

- `max_norm = 5`

---

## 4. Task-Specific Configuration Details

## 4.1 Anomaly Detection

### Baselines Used
- Autoformer
- Informer
- TimesNet

### Windowing
For anomaly detection, non-overlapping windows are used:

- `seq_len = 512`
- `stride = 512`

### Objective
The task is treated as reconstruction-based anomaly detection over fixed windows. Evaluation is based on anomaly scores derived from reconstruction behavior and reported using Adjusted F1. 

---

## 4.2 Classification

### Baselines Used
- Informer
- TimesNet
- 1D-CNN
- LSTM

### Windowing
For classification, the stride depends on the dataset and the temporal density of the sequences. Representative stride values include:

- `stride = 8`
- `stride = 16`
- `stride = 32`
- `stride = 64`

A typical input sequence length (window size) is:

- `seq_len = 512`

### Loss
Classification models are trained using cross-entropy loss.

### Notes
Task targets depend on the dataset. For example, classification may correspond to:
- location
- mobility
- anomaly
- root-cause
- congestion
- coverage
- services
- slice type

The exact supported labels are determined by the selected dataset and task split. 

---

## 4.3 Forecasting

### Baselines Used
- Autoformer
- Informer
- TimesNet
- 1D-CNN
- LSTM
- ETS
- ARIMA

### Windowing and Horizons
For forecasting, a fixed historical context is used together with multiple prediction horizons.

Representative forecasting horizons are:

- `horizon = 32`
- `horizon = 64`
- `horizon = 128`
- `horizon = 208`

The stride depends on the dataset and may vary across:

- `stride = 8`
- `stride = 16`
- `stride = 32`
- `stride = 64`

### Loss
Forecasting models are trained by minimizing mean squared error (MSE).

### Metrics
Forecasting is reported using:

- MSE
- MAE 

---

## 4.4 Imputation

### Baselines Used
- Forward Fill
- Mean
- Nearest Neighbors
- Linear
- Rolling Mean

### Windowing
For imputation, non-overlapping windows are used:

- `seq_len = 512`
- `stride = 512`

### Masking Ratios
Representative masking ratios are:

- `10%`
- `30%`
- `50%`

### Loss
Learned imputation models are optimized by minimizing mean squared error (MSE).

### Metrics
Imputation is reported using:

- MSE
- MAE 

---

## 5. Practical Notes

- The channel dimensionality `C` depends on the selected dataset.
- The same model family may use slightly different effective settings depending on task and memory constraints.
- The reported configurations are intended to document the baseline setup used for the paper and to provide a practical reference for extension and reproduction.
- For larger datasets or longer traces, users may reduce batch size or stride to fit the available GPU memory budget.

---
