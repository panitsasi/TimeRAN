import numpy as np
from ARIMA import load_univariate_series
from statsmodels.tsa.statespace.sarimax import SARIMAX

def run_sarima(
    train_path,
    test_path,
    order=(2, 1, 2),
    seasonal_order=(1, 1, 1, 24),
):

    train_series = load_univariate_series(train_path)
    test_series  = load_univariate_series(test_path)

    model = SARIMAX(
        train_series,
        order=order,
        seasonal_order=seasonal_order,
        enforce_stationarity=False,
        enforce_invertibility=False,
    )
    fit = model.fit(disp=False)
    preds = fit.forecast(steps=len(test_series))
    preds = np.asarray(preds, dtype=float)
    y_true = np.asarray(test_series, dtype=float)
    mae = np.mean(np.abs(y_true - preds))
    rmse = np.sqrt(np.mean((y_true - preds) ** 2))
    return mae, rmse, preds
