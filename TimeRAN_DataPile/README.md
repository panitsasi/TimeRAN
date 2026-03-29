# 🚀 TimeRAN DataPile

> A large-scale, multivariate 5G RAN telemetry corpus for scalable time-series foundation model pretraining and comprehensive downstream wireless analytics tasks.

**TimeRAN DataPile** is a unified large-scale collection of multivariate time-series telemetry designed to support the development of **foundation models for Radio Access Networks (RANs)**. It aggregates measurements from **publicly accessible datasets**, **operational cellular networks**, and **experimental testbeds** into a single benchmark spanning multiple protocol layers, deployment conditions, and downstream tasks.

---

## ✨ Highlights

- 📦 **29 GB** of curated telemetry data
- 📈 **355K unique time series**
- ⏱️ **0.566 billion timestamps**
- 📡 Coverage across **PHY, MAC, RLC, PDCP, and RRC** protocol layers
- 🧠 Supports **anomaly detection, classification, forecasting , and imputation** tasks
- 🌍 Includes data from both **operational networks** and **experimental testbeds**
- 🛠️ Curated for **large-scale pretraining** and **task-specific finetuning**

---


## 📚 Overview

Building large-scale and comprehensive time-series corpora for pretraining **RAN foundation models** remains inherently challenging, despite the growing availability of publicly accessible and open-source datasets. Existing datasets are typically associated with a narrow range of downstream tasks and differ substantially in:

- measurement formats
- temporal resolutions
- channel dimensionality
- protocol-layer visibility
- deployment environments

As a result, current public datasets provide only limited coverage of the diverse operational conditions and temporal behaviors required for large-scale pretraining. This fragmentation restricts the ability to learn **generalizable representations across tasks**, posing a fundamental limitation for training foundation models that rely on broad and diverse time-series data.

To address these challenges, we curate **TimeRAN DataPile**, a unified large-scale RAN telemetry corpus that aggregates time-series measurements across a wide spectrum of RAN-related tasks and experimental settings. To the best of our knowledge, **TimeRAN DataPile** represents one of the most comprehensive collections of RAN time-series data assembled to date.

It consolidates datasets from both **operational networks** and **experimental testbeds** into a unified benchmark while preserving:

- realistic data distributions
- unnormalized measurements
- heterogeneous temporal granularities
- cross-layer observability

---

## 📥 Dataset Download

The **TimeRAN DataPile** dataset is publicly available and can be downloaded as follows:

---

### 1. Navigate to the dataset directory

```
cd TimeRAN/TimeRAN_DataPile
```

---

### 2. Download the dataset

```
gdown 146MSnloH7LyMdY6mdBMEcR7Glil-xEuN -O TimeRAN_DataPile.tar.gz
```

---

### 3. Extract the dataset

```
tar -xvzf TimeRAN_DataPile.tar.gz
```

---

### 4. (Optional) Remove the compressed file

```
rm TimeRAN_DataPile.tar.gz
```

---

### 5. Expected structure

After extraction, the contents should be directly inside:

```
TimeRAN_DataPile/
├── <dataset files and folders>
```

---

> ⚠️ **Note:** The dataset is large (~29 GB). Ensure sufficient disk space before downloading.


## 📊 Corpus Summary

| Property | Value |
|---|---:|
| Total size | 29 GB |
| Unique time series | 355K |
| Total timestamps | 0.566 Billion |
| Core downstream tasks | 4 |
| Protocol layers | PHY, MAC, RLC, PDCP, RRC |

---

## 🧬 Telemetry and Feature Composition

TimeRAN DataPile comprises **heterogeneous multivariate time-series telemetry** capturing RAN behavior across multiple protocol layers and operational dimensions. The data are collected from both:

- 🏢 **Base-station-side measurements**
- 📱 **Device-reported measurements observed at the base station**

The corpus includes telemetry such as:

### PHY Layer
- RSRP
- SINR
- CQI
- link adaptation indicators

### MAC Layer
- PRB utilization
- scheduling statistics
- transport block sizes
- throughput measurements

### RLC Layer
- protocol-level traffic dynamics
- buffering behavior
- retransmission-related indicators

### PDCP Layer
- traffic volume
- flow-level characteristics

### RRC Layer
- connection state
- mobility patterns
- control-plane behavior

Together, these measurements capture both:

- **instantaneous radio conditions**
- **higher-layer traffic and protocol dynamics**

This enables a unified representation of **cross-layer RAN behavior** across diverse wireless environments.

---

## 🎯 Supported Downstream Tasks

A defining characteristic of **TimeRAN DataPile** is its broad support for multiple downstream learning tasks.

### 🔍 Anomaly Detection
Detect disruptive or abnormal network behavior from telemetry streams.

### 🏷️ Classification
Support labeled tasks such as:
- mobility detection
- service classification
- congestion classification
- location classification
- root-cause analysis

### 🧩 Imputation
Recover missing telemetry values from partially observed time series.

### 📈 Forecasting
Predict future network behavior such as:
- PRB utilization
- throughput
- mobility-related dynamics

---

## 🏛️ Protocol-Layer Visibility

TimeRAN DataPile provides observability across multiple layers of the RAN stack:

| Protocol Stack | Representative Supported Tasks |
|---|---|
| **PHY Layer** | Channel quality forecasting, anomaly detection, load-aware energy optimization, interference detection |
| **MAC Layer** | Scheduling optimization, link adaptation optimization, load forecasting, HARQ failure prediction |
| **RLC Layer** | Buffer and queue forecasting, ARQ retransmission forecasting, congestion detection |
| **PDCP Layer** | Throughput prediction, QoS degradation detection, traffic classification |
| **RRC Layer** | Mobility prediction, handover optimization, connection forecasting |

---

## 📦 Dataset Coverage

The corpus aggregates telemetry from the following datasets:

- AERPAW-18 [1]
- AERPAW-20 [2]
- AERPAW-22 [3]
- AERPAW-23 [4]
- AERPAW-24 [5]
- AERPAW-25 [6]
- BLT [7]
- ColO-RAN [8]
- FedJam [9]
- FTSF [10]
- HetNets [11]
- Irish5G [12]
- JamShield [13]
- L5GHDD [14]
- Madrid LTE [15]
- NetData [16]
- NOK [17]
- Open Ireland [18]
- QoE-Aware [19]
- Queens [20]
- Spotlight [21]
- Telecom Italia [22]
- TelecomTS [23]
- Tractor [24]
- WINS [25]

---

## 📋 High-Level Dataset Overview

| Downstream Task | Dataset | Channels | Total Observations | Measurement Granularity |
|---|---|---:|---:|---|
| Anomaly Detection | AERPAW-18 | 4 | 11,694 | Seconds |
| Anomaly Detection | AERPAW-23 | 1 | 1,628 | Seconds |
| Anomaly Detection | BLT | 4 | 259,740 | Weeks |
| Anomaly Detection | HetNets | 1 | 181,818 | Not specified |
| Anomaly Detection | JamShield | 16 | 89,111 | Sub-second |
| Anomaly Detection | NetData | 5 | 20,025,600 | Minutes |
| Anomaly Detection | NOK | 1 | 300,664 | Minutes |
| Anomaly Detection | Spotlight | 191 | 401,663 | Sub-second |
| Anomaly Detection | TelecomTS | 8 | 1,049,976 | Sub-second |
| Classification | AERPAW-20 | 2 | 15,452 | Seconds |
| Classification | Irish5G | 6 | 93,370 | Seconds |
| Classification | JamShield | 16 | 33,777 | Sub-second |
| Classification | QoE-Aware | 3 | 30,925 | Not specified |
| Classification | Spotlight | 191 | 401,663 | Sub-second |
| Classification | TelecomTS | 16 | 329,994 | Sub-second |
| Classification | Tractor | 1 | 1,173,908 | Sub-second |
| Imputation / Forecasting | AERPAW-18 | 4 | 5,847 | Seconds |
| Imputation / Forecasting | AERPAW-20 | 2 | 75,137 | Seconds |
| Imputation / Forecasting | AERPAW-22 | 3 | 6,063 | Seconds |
| Imputation / Forecasting | AERPAW-23 | 1 | 8,140 | Seconds |
| Imputation / Forecasting | AERPAW-24 | 1 | 6,032 | Seconds |
| Imputation / Forecasting | AERPAW-25 | 1 | 56,602 | Seconds |
| Imputation / Forecasting | BLT | 4 | 259,740 | Weeks |
| Imputation / Forecasting | ColO-RAN | 4 | 36,425,436 | Sub-second |
| Imputation / Forecasting | FedJam | 1 | 1,802,238 | Sub-second |
| Imputation / Forecasting | FTSF | 2 | 27,011 | Minutes |
| Imputation / Forecasting | HetNets | 1 | 181,818 | Not specified |
| Imputation / Forecasting | Irish5G | 4 | 96,341 | Seconds |
| Imputation / Forecasting | JamShield | 16 | 29,896 | Sub-second |
| Imputation / Forecasting | L5GHDD | 246 | 9,999 | Not specified |
| Imputation / Forecasting | Madrid LTE | 3 | 4,402,395 | Seconds |
| Imputation / Forecasting | NetData | 5 | 132,138,240 | Minutes |
| Imputation / Forecasting | NOK | 1 | 193,284 | Minutes |
| Imputation / Forecasting | Open Ireland | 4 | 3,175,140 | Sub-second |
| Imputation / Forecasting | QoE-Aware | 3 | 30,925 | Not specified |
| Imputation / Forecasting | Queens | 4 | 346,381 | Seconds |
| Imputation / Forecasting | Spotlight | 191 | 223,143 | Sub-second |
| Imputation / Forecasting | Telecom Italia | 1 | 87,806,617 | Minutes |
| Imputation / Forecasting | TelecomTS | 8 | 1,019,979 | Sub-second |
| Imputation / Forecasting | Tractor | 4 | 54,786 | Sub-second |
| Imputation / Forecasting | WINS | 2 | 779,220 | Sub-second |

---

## 📏 Granularity and Scale

TimeRAN DataPile contains datasets with **heterogeneous temporal resolutions**, ranging from:

- sub-second telemetry
- second-level measurements
- minute-level monitoring
- weekly aggregates

It also spans a wide range of sequence lengths and dimensionalities, from compact low-dimensional traces to high-dimensional cross-layer telemetry.

### Anomaly Detection Subset
- **9 datasets**
- **22,321,894 observations**
- **21,249 unique time series**

Examples:
- **Spotlight**: 191 channels
- **TelecomTS**: 8 channels
- **JamShield**: 16 channels
- **BLT**: weekly measurements
- **NetData / NOK**: minute-level traces

### Classification Subset
- **4,992,037 observations**
- **248 unique time series**

Representative tasks include:
- mobility
- services
- congestion
- zones
- root-cause analysis

Examples:
- **AERPAW-20**: 2 channels
- **Spotlight**: 191 channels

### Imputation / Forecasting Subset
- **269,160,410 observations**
- **166,911 unique time series**

Examples:
- **Telecom Italia**: 1 channel
- **L5GHDD**: 246 channels
- **Open Ireland**: very long traces
- **NetData**: large-scale minute-level telemetry

---

## 🧹 Curation and Preprocessing Pipeline

To address source heterogeneity and ensure reliable downstream learning, TimeRAN DataPile is curated using the following principles:

### 1️⃣ Numeric-only, RAN-relevant feature retention
Only numeric measurements directly reflecting RAN behavior are retained, such as:

- signal quality metrics
- traffic indicators
- scheduling statistics

Auxiliary metadata, identifiers, and inconsistent categorical descriptors are removed.

### 2️⃣ Temporal consistency under multi-file partitioning
Many datasets are distributed across multiple files and folders. We retain only segments that can be **reliably time-synchronized**. Measurements with inconsistent timing or unreliable synchronization are discarded.

### 3️⃣ Removal of redundant or non-informative measurements
We remove channels that are:

- constant
- near-constant
- dominated by zeros
- otherwise non-informative

This avoids inflated dimensionality and improves sequence modeling quality.

### 4️⃣ Handling small or sparse traces
For datasets with fewer than **1,000 samples** or sparse sampling, interpolation may be applied conservatively to improve temporal continuity while preserving local trends.

### 5️⃣ Task-specific augmentation via synthetic anomalies
For a small subset of anomaly-detection datasets where naturally occurring faults are limited or absent, we inject **short-duration synthetic degradations** to enrich anomalous intervals.

This synthetic augmentation is applied to:

- **AERPAW-18**
- **AERPAW-23**
- **BLT**
- **HetNets**
- **NetData**
- **NOK**

For these datasets, anomaly annotations are encoded directly in the file naming convention, where the **last two numerical values** in each filename denote:

- start index of the anomalous interval
- end index of the anomalous interval

Example:

```text
trace_name_1200_1450.csv
```
Here, the anomalous segment spans indices 1200 to 1450.

## 🧪 Task Support Across Datasets

| Dataset | Anomaly Detection | Classification | Imputation | Forecasting |
|---|:---:|:---:|:---:|:---:|
| AERPAW-18 | ✅ | ❌ | ✅ | ✅ |
| AERPAW-20 | ❌ | ✅ | ✅ | ✅ |
| AERPAW-22 | ❌ | ❌ | ✅ | ✅ |
| AERPAW-23 | ✅ | ❌ | ✅ | ✅ |
| AERPAW-24 | ❌ | ❌ | ✅ | ✅ |
| AERPAW-25 | ❌ | ❌ | ✅ | ✅ |
| BLT | ✅ | ❌ | ✅ | ✅ |
| ColO-RAN | ❌ | ❌ | ✅ | ✅ |
| FedJam | ❌ | ❌ | ✅ | ✅ |
| FTSF | ❌ | ❌ | ✅ | ✅ |
| HetNets | ✅ | ❌ | ✅ | ✅ |
| Irish5G | ❌ | ✅ | ✅ | ✅ |
| JamShield | ✅ | ✅ | ✅ | ✅ |
| L5GHDD | ❌ | ❌ | ✅ | ✅ |
| Madrid LTE | ❌ | ❌ | ✅ | ✅ |
| NetData | ✅ | ❌ | ✅ | ✅ |
| NOK | ✅ | ❌ | ✅ | ✅ |
| Open Ireland | ❌ | ❌ | ✅ | ✅ |
| QoE-Aware | ❌ | ✅ | ✅ | ✅ |
| Queens | ❌ | ❌ | ✅ | ✅ |
| Spotlight | ✅ | ✅ | ✅ | ✅ |
| Telecom Italia | ❌ | ❌ | ✅ | ✅ |
| TelecomTS | ✅ | ✅ | ✅ | ✅ |
| Tractor | ❌ | ✅ | ✅ | ✅ |
| WINS | ❌ | ❌ | ✅ | ✅ |

---

## 🧭 Protocol Coverage and Data Provenance

| Dataset | PHY | MAC | RLC | PDCP | RRC | Cross-Layer | Operational Network | Experimental Testbed | Synthetic |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| AERPAW-18 | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ |
| AERPAW-20 | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ |
| AERPAW-22 | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ |
| AERPAW-23 | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ |
| AERPAW-24 | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ |
| AERPAW-25 | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ |
| BLT | ❌ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | ❌ |
| ColO-RAN | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ |
| FedJam | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ |
| FTSF | ❌ | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ |
| HetNets | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |
| Irish5G | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ | ❌ |
| JamShield | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ |
| L5GHDD | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ |
| Madrid LTE | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ |
| NetData | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ |
| NOK | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| Open Ireland | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ |
| QoE-Aware | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| Queens | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ |
| Spotlight | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ |
| Telecom Italia | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ |
| TelecomTS | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ |
| Tractor | ✅ | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ | ✅ | ❌ |
| WINS | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ❌ |

---

## 🧾 Detailed Subset Statistics

### Classification Datasets

| Dataset | Classification Task | Classes | Time Series | Channels | Min Length | Mean Length | Max Length | Total Observations |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| AERPAW-20 | Location | 2 | 4 | 2 | 2266 | 3863 | 5463 | 15452 |
| Irish5G | Mobility | 2 | 40 | 6 | 268 | 2334 | 7190 | 93370 |
| Irish5G | Services | 2 | 40 | 6 | 268 | 2334 | 7190 | 93370 |
| JamShield | Anomaly | 2 | 21 | 16 | 784 | 1608 | 5177 | 33777 |
| QoE-Aware | Handover | 2 | 1 | 3 | 30925 | 30925 | 30925 | 30925 |
| QoE-Aware | Mobility | 2 | 1 | 3 | 30925 | 30925 | 30925 | 30925 |
| Spotlight | Anomaly | 2 | 73 | 191 | 1033 | 5502 | 27678 | 401663 |
| Spotlight | Root Cause Analysis | 4 | 4 | 191 | 7823 | 19836 | 27678 | 79346 |
| TelecomTS | Anomaly | 2 | 5 | 16 | 9999 | 45999 | 99999 | 229995 |
| TelecomTS | Congestion | 2 | 6 | 16 | 9999 | 54999 | 99999 | 329994 |
| TelecomTS | Mobility | 2 | 6 | 16 | 9999 | 54999 | 99999 | 329994 |
| TelecomTS | Services | 3 | 3 | 16 | 99999 | 99999 | 99999 | 299997 |
| TelecomTS | Zones | 3 | 3 | 16 | 99999 | 99999 | 99999 | 299997 |
| Tractor | Services | 9 | 15 | 1 | 4053 | 78260 | 248265 | 1173908 |
| Tractor | Slices | 3 | 26 | 1 | 1770 | 59630 | 248265 | 1550380 |

**Total:** 4,992,037 observations and 248 unique time series.

### Imputation / Forecasting Datasets

| Dataset | Time Series | Channels | Min Length | Mean Length | Max Length | Total Observations |
|---|---:|---:|---:|---:|---:|---:|
| AERPAW-18 | 2 | 4 | 2898 | 2923 | 2949 | 5847 |
| AERPAW-20 | 3 | 2 | 15232 | 25045 | 43566 | 75137 |
| AERPAW-22 | 2 | 3 | 1821 | 3031 | 4242 | 6063 |
| AERPAW-23 | 2 | 1 | 2450 | 4070 | 5690 | 8140 |
| AERPAW-24 | 3 | 1 | 1533 | 2010 | 2421 | 6032 |
| AERPAW-25 | 2 | 1 | 16981 | 28301 | 39621 | 56602 |
| BLT | 180 | 4 | 962 | 1443 | 1924 | 259740 |
| ColO-RAN | 18329 | 4 | 1024 | 1987 | 2226 | 36425436 |
| FedJam | 100 | 1 | 17999 | 18022 | 18034 | 1802238 |
| FTSF | 3 | 2 | 4192 | 9003 | 15927 | 27011 |
| HetNets | 2 | 1 | 54546 | 90909 | 127272 | 181818 |
| Irish5G | 40 | 4 | 1013 | 2408 | 7190 | 96341 |
| JamShield | 14 | 16 | 868 | 2135 | 5177 | 29896 |
| L5GHDD | 2 | 246 | 3000 | 4999 | 6999 | 9999 |
| Madrid LTE | 6 | 3 | 264506 | 733732 | 1260901 | 4402395 |
| NetData | 137644 | 5 | 960 | 960 | 960 | 132138240 |
| NOK | 18 | 1 | 10738 | 10738 | 10738 | 193284 |
| Open Ireland | 2 | 4 | 952542 | 1587570 | 2222598 | 3175140 |
| QoE-Aware | 2 | 3 | 9278 | 15462 | 21647 | 30925 |
| Queens | 57 | 4 | 4092 | 6076 | 9039 | 346381 |
| Spotlight | 57 | 191 | 1184 | 3914 | 4000 | 223143 |
| Telecom Italia | 10000 | 1 | 2883 | 8780 | 8784 | 87806617 |
| TelecomTS | 21 | 8 | 9999 | 48570 | 99999 | 1019979 |
| Tractor | 15 | 4 | 165 | 3652 | 14631 | 54786 |
| WINS | 405 | 2 | 1924 | 1924 | 1924 | 779220 |

**Total:** 269,160,410 observations and 166,911 unique time series.

---

## 🗂️ Why TimeRAN DataPile Matters

TimeRAN DataPile is designed to enable:

- foundation model pretraining for wireless telemetry
- cross-task transfer learning in RAN analytics
- benchmarking across heterogeneous deployment settings
- research on unified representations for wireless systems
- robust evaluation under diverse temporal granularities and channel dimensions

In short, it provides the **scale**, **diversity**, and **cross-layer visibility** needed to move from narrow task-specific models toward **general-purpose RAN foundation models**.

---

## 📚 Dataset References

[1] Ram Asokan, Ozgur Ozdemir, İsmail Güvenç, and Mihail L. Sichitiu, **"Aerial RF and Throughput Measurements on a Non-Standalone 5G Wireless Network,"** *2024 IEEE International Symposium on Dynamic Spectrum Access Networks*, 2024.

[2] Gautham Reddy, Simran Singh, Ismail Guvenc, Mark Poletti, and Ruoyu Sun, **"WIOC: Wireless Indoor-Outdoor Classification Using WiFi and Cellular Signals,"** *2025 IEEE International Conference on Communications Workshops*, 2025.

[3] Simran Singh, **"Android-based 4G LTE Measurements for Semi-Circular UAV Trajectories around a Private AERPAW Base Station,"** dataset, 2024.

[4] Simran Singh, **"Android-based 4G LTE, 5G NR, and Throughput Measurements for Two Sweeps of a UAV near a Private AERPAW Base Station,"** dataset, 2024.

[5] Simran Singh, **"Detailed Cellular and Throughput Measurements for Horizontal Sweeps of a UAV across a Private AERPAW Base Station, using Keysight Nemo and PawPrints,"** dataset, 2024.

[6] Simran Singh, **"Android-based Public 4G LTE Measurements from a Tethered Helikite,"** dataset, 2024.

[7] Luca-Andrei Fechete, Mohamed Sana, Fadhel Ayed, Nicola Piovesan, Wenjie Li, Antonio De Domenico, and Tareq Si Salem, **"Goal-Oriented Time-Series Forecasting: Foundation Framework Design,"** *arXiv:2504.17493*, 2025.

[8] Michele Polese, Leonardo Bonati, Salvatore D'Oro, Stefano Basagni, and Tommaso Melodia, **"ColO-RAN: Developing Machine Learning-Based xApps for Open RAN Closed-Loop Control on Programmable Experimental Platforms,"** *IEEE Transactions on Mobile Computing*, 2023.

[9] Ioannis Panitsas, Iason Ofeidis, and Leandros Tassiulas, **"FedJam: Multimodal Federated Learning Framework for Jamming Detection,"** *arXiv:2508.09369*, 2025.

[10] Vasileios Perifanis, Nikolaos Pavlidis, Remous-Aris Koutsiamanis, and Pavlos S. Efraimidis, **"Federated learning for 5G base station traffic forecasting,"** *Computer Networks*, 2023.

[11] Ilias Chatzistefanidis, Nikos Makris, Virgilios Passas, and Thanasis Korakis, **"ML-based Traffic Steering for Heterogeneous Ultra-dense beyond-5G Networks,"** *2023 IEEE Wireless Communications and Networking Conference*, 2023.

[12] Darijo Raca, Dylan Leahy, Cormac J. Sreenan, and Jason J. Quinlan, **"Beyond throughput, the next generation: a 5G dataset with channel and context metrics,"** *Proceedings of the 11th ACM Multimedia Systems Conference*, 2020.

[13] Ioannis Panitsas, Yagmur Yigit, Leandros Tassiulas, Leandros Maglaras, and Berk Canberk, **"JamShield: A Machine Learning Detection System for Over-the-Air Jamming Attacks,"** *ICC 2025 - IEEE International Conference on Communications*, 2025.

[14] Mukesh Kumar Maheshwari, Alessandro Raschella, Michael Mackay, Max Hashem Eiza, Jon Wetherall, and Jen Laing, **"5G High Density Demand (HDD) Dataset,"** dataset, 2025.

[15] Pablo Fernández Pérez, Claudio Fiandrino, and Joerg Widmer, **"Characterizing and Modeling Mobile Networks User Traffic at Millisecond Level,"** *Proceedings of the 17th ACM Workshop on Wireless Network Testbeds, Experimental Evaluation & Characterization*, 2023.

[16] Yibo Ma, Tong Li, Yuwei Du, Schahram Dustdar, Zhaocheng Wang, and Yong Li, **"Sustainable Connections: Exploring Energy Efficiency in 5G Networks,"** *Proceedings of the 20th International Conference on Emerging Networking EXperiments and Technologies*, 2024.

[17] Pablo Fondo-Ferreiro, Miguel Rodelgo-Lacruz, Francisco Javier González-Castaño, Felipe Gil-Castiñeira, and David Candal-Ventureira, **"Network operator KPIs time series dataset,"** Zenodo, 2023.

[18] Bruno Missi Xavier, Merim Dzaferagic, Magnos Martinello, and Marco Ruffini, **"Performance measurement dataset for open RAN with user mobility and security threats,"** *Computer Networks*, 2024.

[19] Muhammad Kabeer, Rosdiadee Nordin, and Mehran Behjati, **"An Urban Multi-Operator QoE-Aware Dataset for Cellular Networks in Dense Environments,"** Mendeley Data, 2025.

[20] Habiba Elsherbiny, Ahmad M. Nagib, and Hossam S. Hassanein, **"4G LTE User Equipment Measurements along Kingston Transit 502 Bus Route,"** Borealis dataset, 2020.

[21] Chuanhao Sun, Ujjwal Pawar, Molham Khoja, Xenofon Foukas, Mahesh K. Marina, and Bozidar Radunovic, **"SpotLight: Accurate, Explainable and Efficient Anomaly Detection for Open RAN,"** *Proceedings of the 30th Annual International Conference on Mobile Computing and Networking*, 2024.

[22] Gianni Barlacchi, Marco De Nadai, Roberto Larcher, Antonio Casella, Cristiana Chitic, Giovanni Torrisi, Fabrizio Antonelli, Alessandro Vespignani, Alex Pentland, and Bruno Lepri, **"A multi-source dataset of urban life in the city of Milan and the Province of Trentino,"** *Scientific Data*, 2015.

[23] Austin Feng, Andreas Varvarigos, Ioannis Panitsas, Daniela Fernandez, Jinbiao Wei, Yuwei Guo, Jialin Chen, Ali Maatouk, Leandros Tassiulas, and Rex Ying, **"TelecomTS: A Multi-Modal Observability Dataset for Time Series and Language Analysis,"** 2025.

[24] Joshua Groen, Mauro Belgiovine, Utku Demir, Brian Kim, and Kaushik Chowdhury, **"TRACTOR: Traffic Analysis and Classification Tool for Open RAN,"** *ICC 2024 - IEEE International Conference on Communications*, 2024.

[25] Moinak Ghoshal, Omar Basit, Sizhe Wang, Phuc Dinh, Imran Khan, Yufei Feng, Zhekun Yu, Y. Charlie Hu, and Dimitrios Koutsonikolas, **"A First Large-Scale Study of Operational 5G Standalone Networks,"** *Proc. ACM Netw.*, 2025.

---
