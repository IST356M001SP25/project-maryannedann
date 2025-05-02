import plotly.express as px
import pandas as pd
import folium

def create_top_10_cases_bar_chart(df):
    """Create a bar chart for top 10 countries by confirmed cases."""
    top_10_countries = df.nlargest(10, 'total_cases')
    fig = px.bar(top_10_countries, x='country', y='total_cases', 
                 title='Top 10 Countries by Confirmed COVID-19 Cases')
    return fig

def create_cases_pie_chart(df):
    """Create a pie chart for the distribution of confirmed COVID-19 cases."""
    fig = px.pie(df, names='country', values='total_cases', 
                 title='Distribution of Confirmed COVID-19 Cases')
    return fig

def create_historical_line_chart(country, historical_data):
    """Create a line chart for the historical COVID-19 data."""
    dates = [entry['date'] for entry in historical_data['response']]
    total_cases = [entry['cases']['total'] for entry in historical_data['response']]

    df = pd.DataFrame({'Date': dates, 'Total Cases': total_cases})
    fig = px.line(df, x='Date', y='Total Cases', title=f'Historical COVID-19 Cases for {country}')
    return fig
