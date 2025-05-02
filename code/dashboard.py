import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json  # <-- Add this import
from data_extraction import get_statistics_data
from data_transformation import transform_data

# Save data to a file
def save_data_to_file(file_path):
    data = get_statistics_data()
    if data:
        with open(file_path, 'w') as f:
            json.dump(data, f)  # json.dump requires the json module
            print(f"Data saved to {file_path}")
    else:
        print(f"No data to save for {file_path}")

# Function to plot bar charts
def plot_bar_chart(df, metric):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='country', y=metric, data=df)
    plt.title(f'Top 10 Countries by {metric.capitalize()}')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Countries')
    plt.ylabel(metric.capitalize())
    st.pyplot(plt)

# Function to plot line charts
def plot_line_chart(df, metric):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='country', y=metric, data=df)
    plt.title(f'{metric.capitalize()} Trend Over Countries')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Countries')
    plt.ylabel(metric.capitalize())
    st.pyplot(plt)

# Use Streamlit to create a dashboard
def create_dashboard(file_path):
    df = transform_data(file_path)
    if df is not None:
        st.title('COVID-19 Data Visualizations')

        # Display DataFrame
        st.subheader('COVID-19 Statistics by Country')
        st.write(df)

        # Plot Top 10 Countries by Confirmed COVID-19 Cases
        st.subheader('Top 10 Countries by Confirmed COVID-19 Cases')
        top_10_countries = df.nlargest(10, 'cases')  # Ensure 'cases' is the correct column name
        st.write(top_10_countries)

        # Dropdown for selecting different metrics (cases, deaths, recovered)
        st.subheader('Select a Metric')
        metric = st.selectbox('Select Metric', ['cases', 'deaths', 'recovered'])
        
        if metric:
            st.write(f"Showing data for {metric}")
            # Plot Bar Chart for the selected metric
            plot_bar_chart(top_10_countries, metric)

            # Plot Line Chart for the selected metric
            st.subheader(f'{metric.capitalize()} Trend Line')
            plot_line_chart(top_10_countries, metric)

if __name__ == "__main__":
    file_path = 'covid_statistics.json'
    
    # Fetch and save data
    save_data_to_file(file_path)
    
    # Generate dashboard
    create_dashboard(file_path)
