import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def plot(model_name):
    df = pd.read_csv('Volkswagen/online_car-sales.csv')
    new_df = df.dropna(subset=['brand','model','variant','ad_date','city','price'])

    new_df['year'] = pd.to_datetime(new_df['year'], format='%Y')
    model_per_year = new_df.groupby(['year', 'model']).size().unstack().fillna(0)

    st.title(f'Sales for {model_name} per Year')
    st.line_chart(model_per_year[model_name])

if __name__ == "__main__":
    st.set_page_config(page_title='Add')
    df = pd.read_csv('Volkswagen/online_car-sales.csv')
    models = df['model'].unique().tolist()
    selected_model = st.selectbox('Select a model', models)
    plot(selected_model)
