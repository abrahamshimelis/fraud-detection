import numpy as np
import pandas as pd
import socket
import struct
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Function to convert IP address to integer
def ip2int(ip):
    packedIP = socket.inet_aton(ip)
    return struct.unpack("!L", packedIP)[0]

# Define the feature columns (excluding 'signup_time' and 'purchase_time')
feature_columns = ['user_id', 'purchase_value', 'device_id', 'source', 'browser', 'sex', 'age', 'ip_address', 'country', 'transaction_frequency', 'transaction_velocity', 'signup_hour_of_day', 'signup_day_of_week', 'purchase_hour_of_day', 'purchase_day_of_week']

# Preprocess input data
def preprocess_input(data):
    # Convert IP address to integer
    data['ip_address'] = ip2int(data['ip_address'])
    
    # Transaction frequency and velocity (dummy values for the purpose of the example)
    data['transaction_frequency'] = 1
    data['transaction_velocity'] = 0
    
    # Extract hour of day and day of week from 'signup_time' and 'purchase_time'
    data['signup_time'] = pd.to_datetime(data['signup_time'])
    data['signup_hour_of_day'] = data['signup_time'].hour
    data['signup_day_of_week'] = data['signup_time'].dayofweek
    data['purchase_time'] = pd.to_datetime(data['purchase_time'])
    data['purchase_hour_of_day'] = data['purchase_time'].hour
    data['purchase_day_of_week'] = data['purchase_time'].dayofweek

    # Remove the 'signup_time' and 'purchase_time' from the dictionary
    del data['signup_time']
    del data['purchase_time']

    # Create a DataFrame
    df = pd.DataFrame([data])
    
    # Encode categorical features
    le = LabelEncoder()
    for column in ['device_id', 'source', 'browser', 'sex', 'country']:
        df[column] = df[column].astype(str)
        df[column] = le.fit_transform(df[column])
    
    # Scale features
    scaler = MinMaxScaler()
    columns_to_scale = ['user_id', 'purchase_value', 'age', 'ip_address', 'transaction_frequency',
                        'transaction_velocity', 'signup_hour_of_day', 'signup_day_of_week',
                        'purchase_hour_of_day', 'purchase_day_of_week', 'device_id', 'source', 'browser', 'sex', 'country']
    df[columns_to_scale] = scaler.fit_transform(df[columns_to_scale])
    
    # Select the feature columns
    return df[feature_columns]
