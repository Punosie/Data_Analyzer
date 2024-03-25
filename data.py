import pandas as pd

def create_dataFrame(file):
    print('create_dataFrame Called')
    df = pd.read_csv(file)
    new_df = df.dropna()
    return new_df