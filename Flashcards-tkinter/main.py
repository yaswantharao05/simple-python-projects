from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title('Flashy (Flash Cards)')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file='images/card_front.png')
card_back_image = PhotoImage(file='images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)

# ----------------------------- DATAFILE -----------------------------------#
try:
    data_csv = pandas.read_csv('data/french_words_to_learn.csv')
except FileNotFoundError:
    data_csv = pandas.read_csv('data/french_words.csv')
finally:
    # data_list = [{'French': row.French, 'English': row.English}
    #              for (index, row) in data_csv.iterrows()]
    data_list = data_csv.to_dict(orient='records')

# ----------------------------- TEXT ----------------------------------#

language_title = canvas.create_text(400, 150, text='French', font=('Arial', 40, 'italic'))

word = random.choice(data_list)
word_text = canvas.create_text(400, 263, text=word['French'], font=('Arial', 60, 'bold'))


# ----------------------------- BUTTON FUNCTIONS -----------------------#
def next_card():
    # New French word is shown
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(data_list)
    canvas.itemconfig(language_title, text='French', fill='black')
    canvas.itemconfig(word_text, text=word['French'], fill='black')
    canvas.itemconfig(canvas_image, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    # Card is flipped back and English word is shown
    canvas.itemconfig(language_title, text='English', fill='white')
    canvas.itemconfig(word_text, text=word['English'], fill='white')
    canvas.itemconfig(canvas_image, image=card_back_image)


def known_button_clicked():
    if words_left():
        data_list.remove(word)
        data_df = pandas.DataFrame(data_list)
        data_df.to_csv('data/french_words_to_learn.csv', index=False)
        next_card()


def unknown_button_clicked():
    if words_left():
        next_card()


def words_left():
    if len(data_list) != 0:
        return True
    else:
        canvas.itemconfig(language_title, text='OVER!!')
        canvas.itemconfig(word_text, text='All Words Guessed!')
        return False


# ----------------------------- BUTTONS --------------------------------- #
right_button_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_button_image, bg=BACKGROUND_COLOR, command=known_button_clicked,
                      highlightthickness=0)
right_button.grid(column=1, row=1)

wrong_button_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_button_image, bg=BACKGROUND_COLOR, command=unknown_button_clicked,
                      highlightthickness=0)
wrong_button.grid(column=0, row=1)

flip_timer = window.after(3000, func=flip_card)

window.mainloop()
