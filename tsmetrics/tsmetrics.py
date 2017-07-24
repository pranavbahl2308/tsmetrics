# Basic imports
import numpy as np


# ----------------------------Scale independent metrics------------------------

# The mean absolute percentage error (MAPE), is a measure of prediction
# accuracy of a forecasting method in statistics. The 'min_val' variable is
# used to fill zeros in test data, if any. Filling zero with a constant helps
# to avoid division by zero error
def mean_absolute_percentage_error(y_true, y_pred, min_val=0):
    y_true = y_true + min_val
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100


# SMAPE is an alternative for MAPE when there are zeros in the testing data. It
# scales the absolute percentage by the sum of forecast and observed values
def s_mean_absolute_percentage_error(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / ((y_true + y_pred)/2))) * 100


# MAE is used to measure how close the forecast is to observed value
def mean_absolute_error(y_true, y_pred):
    return np.mean(abs(y_true - y_pred))


# MPE represents the percentage of average error occurred, while forecasting.
# It shares similar properties of MAPE except MPE also shows the direction of
# error.
def mean_percentage_error(y_true, y_pred):
    return np.mean((y_true - y_pred) / y_true) * 100


# -----------------------------Scale dependent metrics-------------------------


# In statistics, the mean squared error (MSE) of an estimator measures the
# average of the squares of the errors. The squaring is necessary to remove any
# negative signs. It also gives more weight to larger differences
def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)


# RMSE is the standard deviation of the residuals. It shares the same
# properties as MSE. The square root is used to dampen the magnitude of errors
# caused by squaring them.
def root_mean_squared_error(y_true, y_pred):
    return np.sqrt(np.mean((y_true - y_pred)**2))


# MFE is the difference between observed and forecasted value
def mean_forecast_error(y_true, y_pred):
    return np.mean(y_true - y_pred)


# It measures the total squared deviation of forecasted observations, from the
# observed values
def sum_of_squared_error(y_true, y_pred):
    return np.sum((y_true - y_pred)**2)


# It is same as MSE, except that here the original sign is kept for each
# individual squared error. SMSE panelizes extreme errors, occurred while
# forecasting.
def signed_mean_squared_error(y_true, y_pred):
    error = y_true-y_pred
    return np.mean((error/abs(error))*(error**2))


# NMSE normalizes the obtained MSE after dividing it by the test variance. It
# is a balanced error measure and is very effective in judging forecast
# accuracy of a model.
def normalised_mean_squared_error(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    return mse / (np.sum((y_true - np.mean(y_true)) ** 2)/(len(y_true)-1))


# It is a normalized measure of total forecast error.
def theil_u_statistic(y_true, y_pred):
    error = y_true - y_pred
    mfe = np.sqrt(np.mean(y_pred**2))
    mse = np.sqrt(np.mean(y_true**2))
    rmse = np.sqrt(np.mean(error**2))
    return rmse / (mfe*mse)


# This evaluation metric is used to over come some of the problems of MAPE and
# is used to measure if the forecasting model is better than the naive model or
# not.
def mean_absolute_scaled_error(y_true, y_pred, naive_mod_mae):
    error = y_true - y_pred
    return np.mean(abs(error)/naive_mod_mae)
