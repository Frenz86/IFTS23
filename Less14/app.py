import plotly.express as px
import streamlit as st
from datetime import datetime, date
from meteostat import Point, Daily

def main():
    st.subheader('title')
    start_ = st.date_input(
                            "Start date",
                            date(2019, 7, 6))

    start = datetime(start_.year, start_.month, start_.day)


    end_ = st.date_input(
                        "End date",
                        date(2023, 5, 17))
    
    end = datetime(end_.year, end_.month, end_.day)

    cities = {'Bologna':[44.498955,11.327591]}


    # Create Point for Vancouver, BC
    city = Point(list(cities.values())[0][0],list(cities.values())[0][1], 20)

    # Get daily data for 2018
    df = Daily(city, start, end)
    df = df.fetch()
    df['city'] = list(cities.keys())[0]

    ### ZOOM 

    import plotly.graph_objects as go
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
    fig.update_layout(title = "Titolo",
                    xaxis_title = "Date",
                    yaxis_title = "Sales",
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
                dict(count=2, label="3y", step="year", stepmode="backward"),
                dict(count=10, label="10y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    fig.add_vline(x=date.today(), line_width=3, line_dash="dash", line_color="red")
    fig.update_layout(width=850)
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()