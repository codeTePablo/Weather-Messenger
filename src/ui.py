from src.phrases import recommendations

import random as rn
from tkinter import *
from PIL import Image, ImageTk

THEME_COLOR = "#375362"

#  call this functions from weather (get_weather)


class Interface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Weather Advisor")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(
            text="", bg=THEME_COLOR, font=("Arial", 15, "bold"), fg="white"
        )
        self.score_label.grid(row=0, column=0)

        self.canvas = Canvas(width=300, height=250, bg=THEME_COLOR)
        self.recommendation_text = self.canvas.create_text(
            158,
            125,
            width=280,  #  separete lines
            text="Hi there!",
            font=("Arial", 15, "bold"),
            fill="white",
        )
        self.canvas.grid(row=1, column=0, pady=20)

        image = Image.open("src/images/trebol.png")
        image = image.resize((200, 200), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        self.true_button = Button(
            image=image,
            highlightthickness=0,
            bg=THEME_COLOR,
            command=self.get_next_phrase,
        )  #  Give recommendation
        self.true_button.grid(row=2, column=0)

        self.window.mainloop()

    def get_next_phrase(self):
        weather = rn.choice(list(recommendations))
        # print(weather)
        option = rn.choice(list(recommendations[weather]))
        # print(option)
        text = recommendations[weather][option]
        # print(text)
        self.canvas.itemconfig(self.recommendation_text, text=text)
