import requests


class Weather:
    def __init__(self, my_lat: str, my_lon: str, owm_endpoint: str, api_key: str):
        """
        Insert data from env
        Args:
            self: The instance of the class
            arg1 (str):
            arg2 (str):
            arg3 (str):
            arg4 (str):
        """
        self.my_lat = my_lat
        self.my_lon = my_lon
        self.owm_endpoint = owm_endpoint
        self.api_key = api_key

    def connection_to_api(self):
        """ """
        weather_params = {"lat": self.my_lat, "lon": self.my_lon, "appid": self.api_key}
        response = requests.get(self.owm_endpoint, params=weather_params)
        response.raise_for_status()  #  Check if works connection
        weather_data = response.json()
        # print(weather_data)  #  Json text
        return weather_data

    def get_weather(self):
        """ """
        weather_data = self.connection_to_api()
        weather = weather_data["weather"][0]["description"]
        # print(weather_data)
        return weather

    def get_temperature(self):
        """ """
        weather_data = self.connection_to_api()
        temperature_data = weather_data["main"]["temp"]
        # print(temperature_data)
        temperature = self.convert_temperature(temperature_data)
        return temperature

    def convert_temperature(self, temperature_data):
        """
        kevin to celsius
        """
        # temperature_data = self.get_temperature()
        x = temperature_data - 273.15
        temperature = round(x, 2)
        # print(temperature)
        return temperature
