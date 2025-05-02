import requests

def get_statistics_data():
    url = "https://covid-193.p.rapidapi.com/statistics"
    
    headers = {
        "x-rapidapi-host": "covid-193.p.rapidapi.com",
        "x-rapidapi-key": "bb5c2781bdmshe6e5db32e16701ap180377jsn44f3119b0d83"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch data: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
