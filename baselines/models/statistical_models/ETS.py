import numpy as np
from ARIMA import load_univariate_series

def ewma_forecast(train_series, test_horizon, alpha=0.3):
    train_series = np.asarray(train_series)
    s = train_series[0]
    for x in train_series[1:]:
        s = alpha * x + (1 - alpha) * s
    forecast = np.full(shape=(test_horizon,), fill_value=s, dtype=float)
    return forecast

def run_ewma(train_path, test_path, alpha=0.3):
    train_series = load_univariate_series(train_path)
    test_series  = load_univariate_series(test_path)
    preds = ewma_forecast(train_series, len(test_series), alpha=alpha)
    y_true = test_series
    mae = np.mean(np.abs(y_true - preds))
    rmse = np.sqrt(np.mean((y_true - preds) ** 2))
    return mae, rmse, preds
