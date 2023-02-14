import pandas as pd
import numpy as np


def get_dataset(size):
    # Create Fake Dataset
    df = pd.DataFrame()
    df['size'] = np.random.choice(['big', 'medium', 'small'], size)
    df['age'] = np.random.randint(1, 50, size)
    df['team'] = np.random.choice(['red', 'blue', 'yellow', 'green'], size)
    df['win'] = np.random.choice(['yes', 'no'], size)
    dates = pd.date_range('2020-01-01', '2022-12-31')
    df['date'] = np.random.choice(dates, size)
    df['prob'] = np.random.uniform(0, 1, size)
    return df


def set_dtypes(df):
    df['size'] = df['size'].astype('category')
    df['team'] = df['team'].astype('category')
    df['age'] = df['age'].astype('int16')
    df['win'] = df['win'].map({'yes': True, 'no': False})
    df['prob'] = df['prob'].astype('float32')
    return df


print('Reading and writing CSV')
df = get_dataset(5_000_000)
df = set_dtypes(df)
%time df.to_csv('test.csv')
%time df_csv = pd.read_csv('test.csv')

print('Reading and writing Pickle')
df = get_dataset(5_000_000)
df = set_dtypes(df)
%time df.to_pickle('test.pickle')
%time df_pickle = pd.read_pickle('test.pickle')

print('Reading and writing Parquet')
df = get_dataset(5_000_000)
df = set_dtypes(df)
%time df.to_parquet('test.parquet')
%time df_parquet = pd.read_parquet('test.parquet')

print('Reading and writing Feather')
df = get_dataset(5_000_000)
df = set_dtypes(df)
%time df.to_feather('test.feather')
%time df_feather = pd.read_feather('test.feather')
