import streamlit as st


# Create the interactive elements for the app
st.title("Weather Forecast for the Upcoming Days")  # title
location = st.text_input("Location: ")  # location
days = st.slider("Forecast Days: ", min_value=1, max_value=5
                 , help="Select the number of forecast days")  # slider for days
option = st.selectbox("Pick what weather you want to view "
                      ,("Temperature","Sky Conditions"))  # Allow user to pick weather type
st.subheader(f"Temperature for the next {days} days in {location} ")




