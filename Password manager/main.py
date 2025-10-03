from tkinter import *

window = Tk()
window.title("Password manager")
window.config(padx=20,pady=20)
window.minsize(200,200)

canvas = Canvas(window,width=200,height=200)
canvas.pack()
image_ = PhotoImage(file="C:/tkinter projects/logo.png")
canvas.create_image(100,100,image=image_)

window.mainloop()