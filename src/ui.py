from typing import Tuple
from phrases import recommendations
from models.weather import Weather

# from models.text_message import Message
from twilio.rest import Client

import os
from dotenv import load_dotenv

# import random as rn
from tkinter import *
from PIL import Image, ImageTk

THEME_COLOR = "#375362"


class Interface:
    def __init__(self):
        """
        GUI class for show some data on screen
        """
        self.window = Tk()
        self.window.title("Weather Advisor")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(
            text="", bg=THEME_COLOR, font=("Arial", 15, "bold"), fg="white"
        )
        self.score_label.grid(row=0, column=0)

        self.canvas = Canvas(width=300, height=250, bg=THEME_COLOR)

        self.temperature_weather = self.canvas.create_text(
            158,
            50,
            width=280,  #  separete lines
            text=" ",
            font=("Arial", 15, "bold"),
            fill="white",
        )
        self.canvas.grid(row=1, column=0, pady=10)

        self.recommendation_text = self.canvas.create_text(
            158,
            165,
            width=280,  #  separete lines
            text="Hi there!",
            font=("Arial", 15, "bold"),
            fill="white",
        )
        self.canvas.grid(row=2, column=0, pady=10)

        image = Image.open("images/trebol.png")
        image = image.resize((200, 200), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        self.true_button = Button(
            image=image,
            highlightthickness=0,
            bg=THEME_COLOR,
            command=self.get_next_phrase_and_weather,  #  Give recommendation
        )
        self.true_button.grid(row=3, column=0)

        self.window.mainloop()

    def get_weather(self) -> Tuple[str, int]:
        """
        create model weather with variable environment, return weather and temperature

        Returns:
            tuple(str, int): weather, temperature
        """
        load_dotenv()  #  Load
        my_lat = os.environ["MY_LAT"]
        my_lon = os.environ["MY_LON"]
        owm_endpoint = os.environ["OWM_Endpoint"]
        api_key = os.environ["api_key"]
        weather = Weather(my_lat, my_lon, owm_endpoint, api_key)

        # data = weather.connection_to_api()
        weather_text = weather.get_weather()
        # print(weather_text)
        temperature_text = weather.get_temperature()
        # print(temperature_text)
        return weather_text, temperature_text

    def get_next_phrase_and_weather(self):
        """
        Choice recommendation depending on weather
        """
        get_weather_text = self.get_weather()
        climate_change = get_weather_text[0]
        temperature_change = get_weather_text[1]

        phrase = recommendations[climate_change]["text"]  #  Get recommendation
        # print(phrase)
        if (
            climate_change == "clear sky"
            or "broken clouds"
            or "overcast clouds"
            or "rain"
            or "thunder"
            or "light intensity drizzle"
        ):
            self.send_text_message(
                self.template(climate_change, temperature_change, phrase)
            )

        weather_text = f"Weather: {climate_change}  Temperature: {temperature_change}"

        self.canvas.itemconfig(self.recommendation_text, text=phrase)
        self.canvas.itemconfig(self.temperature_weather, text=weather_text)

    def template(self, weather, temperature, recommendation):
        """
        Message to number destination
        """
        return f"Today will be {weather}, now the temperature is: {temperature}, remember {recommendation}"

    def send_text_message(self, recommendation):
        """
        create connection with twilio
        """
        load_dotenv()  #  Load
        account_sid = os.environ["account_sid"]
        auth_token = os.environ["auth_token"]
        twilio_number = os.environ["twilio_number"]
        destination = os.environ["number"]

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=recommendation,
            from_=twilio_number,
            to=destination,
        )
        # print(message.status)
