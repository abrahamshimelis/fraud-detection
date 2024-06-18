import pandas as pd
import numpy as np

def summarize_categorical(df):
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    categorical_summary = {}
    for col in categorical_cols:
        categorical_summary[col] = df[col].value_counts()
    return categorical_summary

def describe_numerical(df):
    numerical_cols = df.select_dtypes(include=np.number).columns.tolist()
    numerical_stats = df[numerical_cols].describe()
    return numerical_stats

def summarize_time_series(df, date_column):
    # Convert the date column to datetime
    df[date_column] = pd.to_datetime(df[date_column])
    
    # Compute the minimum (start) date, maximum (end) date, and number of unique dates
    min_date = df[date_column].min()
    max_date = df[date_column].max()
    num_unique_dates = df[date_column].nunique()

    # Print the results
    print('Number of Unique Dates:', num_unique_dates)
    print('Start Date:', min_date)
    print('End Date:', max_date)
