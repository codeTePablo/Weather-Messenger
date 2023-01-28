import os
from dotenv import load_dotenv

from src.ui import Interface
from src.models.weather import Weather


class App:
    # load
    load_dotenv()
    my_lat = os.environ["MY_LAT"]
    my_lon = os.environ["MY_LON"]
    owm_endpoint = os.environ["OWM_Endpoint"]
    api_key = os.environ["api_key"]

    ui = Interface()

    weather = Weather(my_lat, my_lon, owm_endpoint, api_key)
    weather.get_weather()
