"""
This file contains the functions that will retrieve and process the data from the weather API.
"""
import requests

API_KEY = "8ca95f091435046e1eb62e88204b3d73"


def get_data(location, forecast_days):
    # Get the data from the API
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Filter the data to access the list of dat contained by the API
    filtered_data = data['list']

    # Further filter the data by forecast days.
    num_values = 8*forecast_days  # There are 8 data points per day in the data.
    filtered_data = filtered_data[:num_values]
    return filtered_data