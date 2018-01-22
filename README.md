# TSMetrics

Welcome!

While building millions of time series models on daily basis I used various commonly used evaluation metrics. I thought putting all of them together as a package could be beneficial for like wise users.

## Installation

You can pip install it straight from git:
```
pip install git+git://github.com:pranavbahl2308/tsmetrics.git
```

## Using tsmetrics

```
from tsmetrics import tsmetrics

true_values = np.array([10,20,30])
predictions = np.array([15,25,35])

rmse = tsmetrics.root_mean_squared_error(true_values, predictions)
```
