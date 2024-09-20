import os
import pandas as pd

def load_data(file_path):
    """Load data from CSV files."""
    return pd.read_csv(file_path, low_memory=False)

def save_data(df, file_path):
    """Save processed data to CSV."""
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    train_data = load_data("../data/raw/train.csv")
    test_data = load_data("../data/raw/test.csv")
    print(f"Train data shape: {train_data.shape}")
    print(f"Test data shape: {test_data.shape}")