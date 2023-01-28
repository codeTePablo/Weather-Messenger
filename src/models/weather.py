import requests


class Weather:
    def __init__(self, my_lat: str, my_lon: str, owm_endpoint: str, api_key: str):
        """
        Insert data from env
        Args:
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
        weather_slice = weather_data["weather"][0]["description"]
        # print(weather_slice)

    def convert_temperature(self):
        """
        kevin to celsius
        """
        weather_data = self.connection_to_api()
        temperature_slice = weather_data["main"]["temp"]
        # print(temperature_slice)
        pass
