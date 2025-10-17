from tkinter import *
import time
from all_fun import Menu

m = Menu()


window = Tk()
window.title("cafe")
window.minsize(height=600,width=600)
window.config(width=600,height=600,padx=20,pady=20,bg="#F5D2D2")

#Cafe Title
heading = Label(
  window,
  text="🍔🥪//🥐🍩Pixel-Cafe🍪🧁//🍕🍟",
  font=("Comic Sans MS",28,"normal"),
  bg="#A3CCDA",
  fg="#F8F7BA",
  padx=10,
  pady=10
  )
heading.grid(column=0,row=0,pady=20,columnspan=2)

#menu
menu = Label(
  window,
  text="What uhh like to have??",
  bg="#F8F7BA",
  font=("Comic Sans MS",20,"normal"),
  fg="#F5D2D2")
menu.grid(column=0,row=1,pady=10)
#pizza
pizza = Button(
  text="Pizza🍕",
  fg="white",
  bg="#A3CCDA",
  font=("Comic Sans MS",11,"normal"),
  width=20,
  command=m.on_click_menu())
pizza.grid(column=0,row=2,pady=10)

#Burger
burger = Button(
  text="Burger🍔",
  fg="white",
  bg="#A3CCDA",
  font=("Comic Sans MS",11,"normal"),
  width=20)
burger.grid(column=0,row=3,pady=10)

#pastry
pastry = Button(
  text="Pastry🍰",
  fg="white",
  bg="#A3CCDA",
  font=("Comic Sans MS",11,"normal"),
  width=20)
pastry.grid(column=0,row=4,pady=10)

#Pasta
pasta = Button(
  text="Pasta🍝",
  fg="white",
  bg="#A3CCDA",
  font=("Comic Sans MS",11,"normal"),
  width=20)
pasta.grid(column=0,row=5,pady=10)

#browine
brownie = Button(
  text="Brownie🍥",
  fg="white",
  bg="#A3CCDA",
  font=("Comic Sans MS",11,"normal"),
  width=20)
brownie.grid(column=0,row=6,pady=10)

#sandwich
sandwich = Button(
  text="Sandwich🥪",
  fg="white",
  bg="#A3CCDA",
  font=("Comic Sans MS",11,"normal"),
  width=20)
sandwich.grid(column=0,row=7,pady=10)



#asking bill
ask_bill = Label(
  window,
  text="Shall I make ur bill??",
  bg="#F8F7BA",
  font=("Comic Sans MS",20,"normal"),
  fg="#F5D2D2")
ask_bill.grid(column=1,row=1,pady=10)


#Yes or no
yeah_sure = Button(
  text="Yeahh Sure!!",
  fg="white",
  bg="#A3CCDA",
  font=("Comic Sans MS",10,"normal"),
  width=30)
yeah_sure.grid(column=1,row=2,pady=10)

#bill
def give_bill():
  bill = Label(window,text="Have a Nice Day!!\n😊😃😄😀🫠\n😋😋",
               bg="#F8F7BA",
    font=("Comic Sans MS",20,"normal"),
    fg="#F5D2D2")
  bill.grid(column=1,row=3,pady=10,rowspan=3)


give_bill = window.after(5000,give_bill())




window.mainloop()