import streamlit as st
import plotly.express as px
from Data_process import *

# Create the interactive elements for the app
st.title("Weather Forecast for the Upcoming Days ☁️")  # title
location = st.text_input("Location: ")  # location
days = st.slider("Forecast Days: ", min_value=1, max_value=5
                 , help="Select the number of forecast days")  # slider for days
option = st.selectbox("Pick what weather you want to view "
                      , ("Temperature 🌡️", "Sky Conditions ⛅️"))  # Allow user to pick weather type
st.subheader(f"Temperature for the next {days} days in {location} ")

# Only call the get data function if a user inputs a place
if location:
    # Get the required data
    filtered_data = get_data(location, days)

    if option == "Temperature 🌡️":
        temperatures = [dict['main']['temp'] for dict in filtered_data]
        dates = [dict['dt_txt'] for dict in filtered_data]
        # Add a plot for temperature data
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Sky Conditions ⛅️":
        images = {"Clear":"images/clear.png","Clouds":"images/cloud.png",
                  "Rain":"images/rain.png","Snow":"images/snow.png"}
        sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        st.image(image_paths,width=115)
