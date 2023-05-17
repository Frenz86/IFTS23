import streamlit as st
import pandas as pd
from datetime import datetime, date
from meteostat import Point, Daily
import pandas as pd
import plotly.graph_objects as go
from geopy.geocoders import Nominatim

def main():
    st.header("Weather")
    citta = st.text_input("Inserisci il nome della città", value="Bologna")

    geolocator = Nominatim(user_agent="Your_name")
    location = geolocator.geocode(citta)

    # lat = st.number_input("Inserisci la latitudine", value=44.498955, format="%6f")
    # long = st.number_input("Inserisci la longitudine", value=11.327591, format="%6f")
    data_inizio = st.date_input("Inserisci la data di inizio", date(2019,7,6))
    data_fine = st.date_input("Inserisci la data di fine", date(2023,5,17))

    start = datetime(data_inizio.year, data_inizio.month, data_inizio.day)
    end = datetime(data_fine.year, data_fine.month, data_fine.day)

    cities = {citta:[location.latitude,location.longitude]}
    city = Point(list(cities.values())[0][0],list(cities.values())[0][1], 20)

    df = Daily(city, start, end)
    df = df.fetch()
    df['city'] = list(cities.keys())[0]


    fig = go.Figure()
    #Actual 
    fig.add_trace(go.Scatter(x = df.index, 
                            y = df['tavg'],
                            mode = "lines",
                            name = "Aveg",
                            line_color='#0000FF',
                            ))
    ##############################################################
    #Predicted 
    fig.add_trace(go.Scatter(x = df.index, 
                            y = df['tmax'],
                            mode = "lines", 
                            name = "Max",
                            line_color='#ff8c00',
                            ))

    ##############################################################
    # adjust layout
    fig.update_layout(title = f"Temperatura di {citta} dal  {start.date()}  al {end.date()}",
                    xaxis_title = "Date",
                    yaxis_title = "Temperature °C",
                    width = 1700,
                    height = 700,
                    )
    ####################################################################
    # zoomming
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(count=3, label="3y", step="year", stepmode="backward"),
                dict(count=10, label="10y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    fig.add_vline(x=date.today(), line_width=3, line_dash="dash", line_color="red")
    fig.update_layout(width=850)
    st.plotly_chart(fig)
    st.map(pd.DataFrame({'lat' : [location.latitude] , 'lon' : [location.longitude]},columns = ['lat','lon']))

if __name__ == "__main__":
    main()