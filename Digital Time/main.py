from tkinter import *

window = Tk()
window.config(width=500,height=500,bg="#91C4C3",padx=20,pady=20)
window.minsize(height=500,width=500)

#Lable 
clock = Label(text="TIMER",bg="#91C4C3",font=("Cascadia Mono",27,"bold"),fg="#FFF7DD")
clock.pack()

#time
time = Label(text="00:00 am",bg="#91C4C3",font=("Cascadia Mono",29,"bold"),fg="#FFF7DD")
time.pack()

window.mainloop()