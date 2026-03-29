import numpy as np
from ARIMA import load_univariate_series
from statsmodels.tsa.holtwinters import ExponentialSmoothing


def run_holt_winters(
    train_path,
    test_path,
    trend="add",
    seasonal=None,
    seasonal_periods=None,
):
    train_series = load_univariate_series(train_path)
    test_series  = load_univariate_series(test_path)

    model = ExponentialSmoothing(
        train_series,
        trend=trend,
        seasonal=seasonal,
        seasonal_periods=seasonal_periods,
    )
    fit = model.fit(optimized=True)

    preds = fit.forecast(steps=len(test_series))

    preds = np.asarray(preds, dtype=float)
    y_true = np.asarray(test_series, dtype=float)

    mae = np.mean(np.abs(y_true - preds))
    rmse = np.sqrt(np.mean((y_true - preds) ** 2))

    return mae, rmse, preds
