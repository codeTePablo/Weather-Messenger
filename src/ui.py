from src.phrases import recommendations
from src.models.weather import Weather

import os
from dotenv import load_dotenv

import random as rn
from tkinter import *
from PIL import Image, ImageTk

THEME_COLOR = "#375362"

#  call this functions from weather (get_weather)


class Interface:
    def __init__(self):
        """ """
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
            text="Temperature: \nWeather: ",
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

        image = Image.open("src/images/trebol.png")
        image = image.resize((200, 200), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        self.true_button = Button(
            image=image,
            highlightthickness=0,
            bg=THEME_COLOR,
            command=self.get_next_phrase,
        )  #  Give recommendation
        self.true_button.grid(row=3, column=0)

        self.window.mainloop()

    def get_weather(self):
        """ """
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

        return f"Weather: {weather_text}    Temperature: {temperature_text}"

    def get_next_phrase(self):
        """ """
        weather = rn.choice(list(recommendations))
        # print(weather)
        text = rn.choice(list(recommendations[weather]))
        # print(text)
        phrases = recommendations[weather][text]
        # print(phrases)

        weather_text = self.get_weather()
        # print(weather_text)

        self.canvas.itemconfig(self.recommendation_text, text=phrases)
        self.canvas.itemconfig(self.temperature_weather, text=weather_text)
