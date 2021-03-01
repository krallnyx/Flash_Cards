from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


class FlashCards:

    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
        data = pandas.read_csv("data/french_words.csv")
        self.dict = data.to_dict(orient="records")
        self.card_title = None
        self.card_word = None
        self.create_layout()

    def create_layout(self):

        self.window.title("Flash Cards")
        self.window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

        self.canvas.card_front_image = PhotoImage(file="images/card_front.png")
        self.canvas.create_image(400, 263, image=self.canvas.card_front_image)
        self.card_title = self.canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
        self.card_word = self.canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
        self.canvas.grid(column=0, row=0, columnspan=2)

        self.canvas.right_image = PhotoImage(file="images/right.png")
        right_button = Button(image=self.canvas.right_image, highlightthickness=0, command=self.create_new_card)
        right_button.grid(column=1, row=1)
        self.canvas.wrong_image = PhotoImage(file="images/wrong.png")
        wrong_button = Button(image=self.canvas.wrong_image, highlightthickness=0, command=self.create_new_card)
        wrong_button.grid(column=0, row=1)
        self.create_new_card()

    def create_new_card(self):
        self.canvas.itemconfig(self.card_title, text="French")
        self.canvas.itemconfig(self.card_word, text=random.choice(self.dict)["French"])


if __name__ == '__main__':
    flash_cards = FlashCards()

    flash_cards.window.mainloop()
