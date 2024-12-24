#!/usr/bin/env python
# coding: utf-8

# ## Standard package imports

# In[7]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Save merged_data to a pickle file
if __name__ == "__main__":
    with open('merged_data.pkl', 'wb') as f:
        pickle.dump(merged_data, f)


def preprocess_and_split_data(merged_data, target_column='Unified_Diabetes', test_size=0.2):
    """
    Preprocesses the data by handling missing values, converting boolean columns to integers,
    and splitting the data into train and test sets.

    Parameters:
    - merged_data: The final cleaned DataFrame with features and target.
    - target_column: The column name that will be the target variable (default: 'Unified_Diabetes').
    - test_size: The proportion of the data to be used for testing (default: 0.2).

    Returns:
    - X_train, X_test, y_train, y_test: The training and testing data splits for features and target.
    """
    # Prepare features and target variable
    X = merged_data.drop(columns=[target_column])

    # Convert boolean columns to integers
    for col in X.columns:
        if X[col].dtype == 'bool':
            X[col] = X[col].astype(int)

    # Handle missing values by dropping rows with NaN values
    X = X.dropna()

    y = merged_data[target_column]

    # Split into training and testing sets (e.g., 80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    return X_train, X_test, y_train, y_test

