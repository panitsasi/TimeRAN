import numpy as np
from ARIMA import load_univariate_series  

def moving_average_forecast(series, window=10):
    series = np.asarray(series)
    n = len(series)
    preds = []

    for i in range(window, n):
        history = series[i - window:i]
        preds.append(history.mean())

    return np.array(preds)

def run_moving_average(train_path, test_path, window=10):
    train_series = load_univariate_series(train_path)
    test_series  = load_univariate_series(test_path)
    full = np.concatenate([train_series, test_series])
    total_len = len(full)
    if len(train_series) < window:
        raise ValueError(f"Train length {len(train_series)} < window {window}")

    start_test_idx = len(train_series)
    preds = []
    for i in range(start_test_idx, total_len):
        history = full[i - window:i]
        preds.append(history.mean())

    preds = np.asarray(preds)
    y_true = test_series
    mae = np.mean(np.abs(y_true - preds))
    rmse = np.sqrt(np.mean((y_true - preds) ** 2))
    return mae, rmse, preds
