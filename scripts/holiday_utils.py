import numpy as np
import pandas as pd

def days_to_next_holiday(date, holiday_dates):
    """
    Calculate the number of days to the next holiday.
    
    Args:
    date (datetime): The current date.
    holiday_dates (list): A list of holiday dates as pandas datetime objects.
    
    Returns:
    int or np.nan: The number of days to the next holiday, or NaN if no future holiday exists.
    """
    future_holidays = [holiday for holiday in holiday_dates if holiday > date]
    if future_holidays:
        return (min(future_holidays) - date).days
    else:
        return np.nan

def days_after_last_holiday(date, holiday_dates):
    """
    Calculate the number of days after the last holiday.
    
    Args:
    date (datetime): The current date.
    holiday_dates (list): A list of holiday dates as pandas datetime objects.
    
    Returns:
    int or np.nan: The number of days after the last holiday, or NaN if no past holiday exists.
    """
    past_holidays = [holiday for holiday in holiday_dates if holiday < date]
    if past_holidays:
        return (date - max(past_holidays)).days
    else:
        return np.nan
