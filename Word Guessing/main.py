from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("C:/tkinter projects/Word Guessing/CSV files/Kannada_to_English_Easy.csv")
def on_correct_click():
  random_k_word = random.choice(data["Kannada"])
  canvas.itemconfig(main_k_word,text=random_k_word)
  canvas.itemconfig(k_heading,text="ಕನ್ನಡ")


window = Tk()
window.title("Word Guess")
window.config(width=800,height=526,padx=50,pady=50,bg=BACKGROUND_COLOR)

#card image
canvas = Canvas(window,width=800,height=526)
canvas.grid(column=0,row=0,columnspan=2)
card_image = PhotoImage("C:/tkinter projects/Word Guessing/images/card_front.png")
canvas.create_image(400,263,image=card_image)
k_heading = canvas.create_text(400,150,text="Title",font=("Arial",40,"normal"))
main_k_word = canvas.create_text(400,263,text="Word",font=("Arial",60,"bold"))

#Correct button
correct_image = PhotoImage(file="C:/tkinter projects/Word Guessing/images/right.png")
correct_button = Button(image=correct_image,highlightthickness=0,command=on_correct_click)
correct_button.grid(column=1,row=1)

#Wrong button
wrong_image = PhotoImage(file="C:/tkinter projects/Word Guessing/images/wrong.png",)
wrong_button = Button(image=wrong_image,highlightthickness=0)
wrong_button.grid(column=0,row=1)

window.mainloop()