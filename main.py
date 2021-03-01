from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


def flash_cards():
    window = Tk()
    window.title("Flash Cards")
    window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

    canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
    card_front_image = PhotoImage(file="images/card_front.png")
    canvas.create_image(400, 263, image=card_front_image)
    canvas.create_text(400, 150, text="Language", font=("Arial", 40, "italic"))
    canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
    canvas.grid(column=0, row=0, columnspan=2)

    right_image = PhotoImage(file="images/right.png")
    right_button = Button(image=right_image, highlightthickness=0)
    right_button.grid(column=1, row=1)
    wrong_image = PhotoImage(file="images/wrong.png")
    wrong_button = Button(image=wrong_image, highlightthickness=0)
    wrong_button.grid(column=0, row=1)

    window.mainloop()


if __name__ == '__main__':
    flash_cards()
