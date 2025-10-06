from tkinter import *
import time as tm

def update_time():
  current_time = tm.strftime("%I:%M:%S %p")
  time.config(text=current_time)
  window.after(1000,update_time)

window = Tk()
window.config(width=500,height=500,bg="#91C4C3",padx=20,pady=20)
window.minsize(height=500,width=500)

#Lable 
clock = Label(text="Clock",bg="#91C4C3",font=("Cascadia Mono",27,"bold"),fg="#FFF7DD")
clock.pack()

#time
time = Label(text="00:00 am",bg="#91C4C3",font=("Cascadia Mono",29,"bold"),fg="#FFF7DD")
time.pack()

update_time()

window.mainloop()