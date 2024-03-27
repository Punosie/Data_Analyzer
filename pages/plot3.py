import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def plot():
    df = pd.read_csv('Volkswagen/online_car-sales.csv')
    new_df = df.dropna(subset=['brand','model','variant','ad_date','city','price'])

    new_df['year'] = pd.to_datetime(new_df['year'], format='%Y')

    unique_models = new_df['model'].unique()

    st.title('Model sold per Year')
    
    for model in unique_models:
        model_data = new_df[new_df['model'] == model].groupby('year').size()
        fig, ax = plt.subplots()
        ax.plot(model_data.index, model_data.values)
        ax.set_title(f'{model} sold per Year')
        ax.set_xlabel('Years')
        ax.set_ylabel('Cars')
        ax.grid(True)
        st.pyplot(fig)

if __name__ == "__main__":
    st.set_page_config(page_title='Add')
    plot()
