import pandas as pd
import matplotlib.pyplot as plt

def create_dataFrame(file):
    print('create_dataFrame Called')
    df = pd.read_csv(file)
    new_df = df.dropna()
    return new_df

def display_data():
    print('display_data Called')
    df = create_dataFrame(df)
    return df.head(5)

def set_date_column(df, date):
    print('set_date_column Called')
    df.loc[:,f'{date}'] = pd.to_datetime(df[f'{date}'])

def set_analysis_field(df, field):
    print('set_analysis_field Called')
    sold_models = df[f'{field}'].value_counts()
    return sold_models

def plot_graph(df, time, field, graph_type):
    df[f'{time}'] = pd.to_datetime(df[f'{time}'], format='%Y')
    model_per_year = df.groupby([f'{time}', f'{field}']).size()
    model_per_year.plot(kind=f'{graph_type}')
    plt.figure(figsize=(40, 6))
    plt.title('Model sold per Year')
    plt.xlabel('Years')
    plt.ylabel('Cars')
    plt.grid(True)
    plt.show()