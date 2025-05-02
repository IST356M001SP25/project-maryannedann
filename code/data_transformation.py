import pandas as pd
import json

def transform_data(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        countries_data = data['response']  # Extracting country data from the API response
        country_stats = []

        for country in countries_data:
            country_info = {
                "country": country['country'],
                "cases": country['cases']['total'],
                "deaths": country['deaths']['total'],
                "recovered": country['cases']['recovered'],
                "critical": country['cases']['critical'],
                "active": country['cases']['active'],
                "population": country['population']
            }
            country_stats.append(country_info)

        df = pd.DataFrame(country_stats)
        return df
    except Exception as e:
        print(f"Error transforming data: {e}")
        return None
