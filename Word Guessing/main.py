from tkinter import *
import pandas as pd
import random
import time
BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("C:/tkinter projects/Word Guessing/CSV files/Kannada_to_English_Easy.csv")
to_learn = data.to_dict(orient="records")
current_slide = {}


def on_correct_click():
  global current_slide, flip_timer
  window.after_cancel(flip_timer)
  current_slide = random.choice(to_learn)
  random_k_word = current_slide["Kannada"]
  canvas.itemconfig(main_k_word,text=random_k_word)
  canvas.itemconfig(k_heading,text="ಕನ್ನಡ")
  canvas.itemconfig(bg_image,image=front_card)
  flip_timer = window.after(3000,flipped_card)

def flipped_card():
  same_e_word = current_slide["English"]
  canvas.itemconfig(main_k_word,text=same_e_word)
  canvas.itemconfig(k_heading,text="English")
  canvas.itemconfig(bg_image,image=back_card)
  
def is_known():
  to_learn.remove(current_slide)
  on_correct_click()



window = Tk()
window.title("Word Guess")
window.config(width=800,height=526,padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,flipped_card)

#card image
canvas = Canvas(window,width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)
front_card = PhotoImage(file="C:/tkinter projects/Word Guessing/images/card_front.png")
back_card = PhotoImage(file="C:/tkinter projects/Word Guessing/images/card_back.png")
bg_image = canvas.create_image(400,263,image=front_card)
k_heading = canvas.create_text(400,150,text="Title",font=("Arial",40,"normal"))
main_k_word = canvas.create_text(400,263,text="Word",font=("Arial",60,"bold"))

#Correct button
correct_image = PhotoImage(file="C:/tkinter projects/Word Guessing/images/right.png")
correct_button = Button(image=correct_image,highlightthickness=0,command=is_known)
correct_button.grid(column=1,row=1)

#Wrong button
wrong_image = PhotoImage(file="C:/tkinter projects/Word Guessing/images/wrong.png",)
wrong_button = Button(image=wrong_image,highlightthickness=0,command=on_correct_click)
wrong_button.grid(column=0,row=1)

on_correct_click()



window.mainloop()