from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


class FlashCards:

    def __init__(self):
        self.window = Tk()
        self.canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
        try:
            data = pandas.read_csv("data/words_to_learn.csv")
        except FileNotFoundError:
            data = pandas.read_csv("data/french_words.csv")
        self.dict = data.to_dict(orient="records")
        self.card_title = None
        self.card_word = None
        self.create_layout()
        self.flip_timer = self.window.after(3000, func=self.flip_card)

    def create_layout(self):

        self.window.title("Flash Cards")
        self.window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

        self.canvas.card_front_image = PhotoImage(file="images/card_front.png")
        self.canvas.card_back_image = PhotoImage(file="images/card_back.png")
        self.card_background = self.canvas.create_image(400, 263)
        self.card_title = self.canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
        self.card_word = self.canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
        self.canvas.grid(column=0, row=0, columnspan=2)

        self.canvas.right_image = PhotoImage(file="images/right.png")
        right_button = Button(image=self.canvas.right_image, highlightthickness=0, command=self.remove_from_list)
        right_button.grid(column=1, row=1)
        self.canvas.wrong_image = PhotoImage(file="images/wrong.png")
        wrong_button = Button(image=self.canvas.wrong_image, highlightthickness=0, command=self.create_new_card)
        wrong_button.grid(column=0, row=1)
        self.create_new_card()

    def create_new_card(self):
        try:
            self.window.after_cancel(self.flip_timer)
        except AttributeError:
            pass
        if len(self.dict) > 0:
            self.current_card = random.choice(self.dict)

        else:
            messagebox.showinfo(title="Congratulations", message="You know all the words from the list.\n"
                                                                 "The list will now be reset to it's original content.")
            data = pandas.read_csv("data/french_words.csv")
            self.dict = data.to_dict(orient="records")
        self.canvas.itemconfig(self.card_background, image=self.canvas.card_front_image)
        self.canvas.itemconfig(self.card_title, text="French", fill="black")
        self.canvas.itemconfig(self.card_word, text=self.current_card["French"], fill="black")
        self.flip_timer = self.window.after(3000, func=self.flip_card)

    def flip_card(self):
        self.canvas.itemconfig(self.card_title, text="English", fill="white")
        self.canvas.itemconfig(self.card_word, text=self.current_card["English"], fill="white")
        self.canvas.itemconfig(self.card_background, image=self.canvas.card_back_image)

    def remove_from_list(self):
        self.dict.remove(self.current_card)
        data = pandas.DataFrame(self.dict)
        data.to_csv("data/words_to_learn.csv", index=False)
        self.create_new_card()


if __name__ == '__main__':
    flash_cards = FlashCards()
    flash_cards.window.mainloop()
