import pandas as pd
import matplotlib.pyplot as plt

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