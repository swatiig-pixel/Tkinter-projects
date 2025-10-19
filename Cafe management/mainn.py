from all_fun import *
from tkinter import *

def on_click_menu():
  MenuWindow(window)
  


window = Tk()
window.title("cafe")
window.minsize(height=600,width=600)
window.config(width=600,height=600,padx=20,pady=20,bg="#F5D2D2")

heading = Label(
  window,
  text="🍔🥪//🥐🍩Pixel-Cafe🍪🧁//🍕🍟",
  font=("Comic Sans MS",25,"normal"),
  bg="#A3CCDA",
  fg="#F8F7BA",
  padx=10,
  pady=10
  )
heading.place(relx=0.5,rely=0.05,anchor="n")

menu_bar = Button(window,text="Menu",
                  font=("Comic Sans MS",20,"normal"),
                  bg="#F8F7BA",
                  fg="#F5D2D2",
                  command=on_click_menu)
menu_bar.place(relx=0.5,rely=0.45,anchor="center")






window.mainloop()