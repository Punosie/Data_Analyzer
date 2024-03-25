import streamlit as st
from app import plot_graph, set_date_column, set_analysis_field
from data import create_dataFrame

# Cache the create_dataFrame function
@st.cache_data
def cached_create_dataFrame(file):
    return create_dataFrame(file)

def add():
    st.subheader("Import the Dataset")
    file = st.file_uploader('Upload CSV file', type=['csv'])
    if file is not None:
        df = cached_create_dataFrame(file)  # Use cached function
        st.success('File Uploaded Successfully')
        st.dataframe(df.head())
        return df
    else:
        st.warning("Please upload a CSV file.")
        return None

def plot():
    st.header('Plot')
    df = add()

    if df is not None:
        time_in = st.text_input('Time')
        field_in = st.text_input('Field')
        graph_type = st.radio('Graph Type', ['bar', 'area', 'pie'])

        # Button to plot the graph
        if st.button("Plot Graph"):
            if time_in and field_in:  # Check if both time and field inputs are provided
                time = set_date_column(df, time_in)
                field = set_analysis_field(df, field_in)
                plot_graph(df, time, field, graph_type)
            else:
                st.warning("Please enter values for 'Time' and 'Field' to plot the graph.")

if __name__ == "__main__":
    st.set_page_config(page_title='Add')
    plot()
