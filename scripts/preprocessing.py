import pandas as pd
import numpy as np
import logging

def handle_missing_values(df, is_train=True):
    """
    Fills missing values in the dataframe if the column exists.
    :param df: Input dataframe.
    :param is_train: Boolean indicating whether the dataframe is train or test.
    """
    if 'CompetitionOpenSinceMonth' in df.columns:
        df['CompetitionOpenSinceMonth'].fillna(0, inplace=True)
    if 'CompetitionOpenSinceYear' in df.columns:
        df['CompetitionOpenSinceYear'].fillna(0, inplace=True)
    if 'Promo2SinceWeek' in df.columns:
        df['Promo2SinceWeek'].fillna(0, inplace=True)
    if 'Promo2SinceYear' in df.columns:
        df['Promo2SinceYear'].fillna(0, inplace=True)
    if 'PromoInterval' in df.columns:
        df['PromoInterval'].fillna('None', inplace=True)
    
    # Only handle 'Open' column in test dataset
    if not is_train and 'Open' in df.columns:
        df['Open'].fillna(df['Open'].mode()[0], inplace=True)
    
    return df

def convert_dtypes(df):
    """
    Converts columns to appropriate data types.
    :param df: Input dataframe.
    """
    if 'StateHoliday' in df.columns:
        df['StateHoliday'] = df['StateHoliday'].astype('category')
    return df

def process_dates(df):
    """
    Converts 'Date' column to datetime.
    :param df: Input dataframe.
    """
    if "Date" in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
    return df

def preprocess_data(df, is_train=True):
    """
    Preprocess the input dataframe by handling missing values, converting data types, and processing dates.
    :param df: Input dataframe.
    :param is_train: Boolean indicating whether the dataframe is train or test.
    """
    df = handle_missing_values(df, is_train)
    df = convert_dtypes(df)
    df = process_dates(df)
    
    return df

def handle_outliers(df):
    """
    Detects and handles outliers in the dataset.
    :param df: Input dataframe
    """
    logging.info("Detecting outliers in sales data...")
    # Example: Removing sales outliers based on Z-score
    z_scores = np.abs((df['Sales'] - df['Sales'].mean()) / df['Sales'].std())
    df = df[z_scores < 3]  # Keeping only data with Z-scores < 3 (within 3 standard deviations)
    
    logging.info("Outliers detected and handled.")
    return df

def feature_engineering(df):
    df = df.copy()  # Ensure you're working on a copy to avoid chained assignments
    
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    
    # Add other feature engineering steps here
    
    return df
