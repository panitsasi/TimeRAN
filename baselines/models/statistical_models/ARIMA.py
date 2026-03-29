import json
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error

def load_univariate_series(jsonl_path):
    values_all = []

    with open(jsonl_path, "r") as f:
        for line in f:
            item = json.loads(line)
            keys = item["KPIs"]["keys"]
            vals = item["KPIs"]["values"]
            idx = None
            for i, k in enumerate(keys):
                if k not in ["UL_Protocol", "DL_Protocol"]:
                    idx = i
                    break

            if idx is None:
                continue

            segment = vals[idx]
            values_all.extend(segment)

    return np.array(values_all, dtype=np.float32)


def run_arima(train_path, test_path, order=(2,1,2)):

    train_series = load_univariate_series(train_path)
    test_series  = load_univariate_series(test_path)

    model = ARIMA(train_series, order=order)
    fitted = model.fit()

    n_test = len(test_series)
    forecast = fitted.forecast(steps=n_test)

    mae = mean_absolute_error(test_series, forecast)
    mse  = mean_squared_error(test_series, forecast)
    rmse = np.sqrt(mse)
    
    return mae, rmse, forecast
