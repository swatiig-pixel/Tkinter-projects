from tkinter import *
from tkinter import ttk

MENU_FONT = ("Comic Sans MS",11,"normal")

class MenuWindow(Tk):

  def __init__(self):
    super().__init__()
    self.title("Menu")
    self.minsize(width=600,height=600)
    
  def heading(self):
    pick = ttk.Label(text="Pick Whatever uhh wantt!!!",font=("Comic Sans MS",28,"normal"),)
    pick.grid(column=0,row=0,columnspan=5)

  def western_buttons(self):
    dish_list = ["Pizza🍕","Burger🍔","Sandwich🥪","Pasta🍝","Pastry🍰","Brownie🍥","Momos🥟","Waffle🧇","Donots🍩"]
    for i,each in enumerate(dish_list):
      west_menu = (ttk.Button(text=each,))
      west_menu.grid(row=i+1,column=0)
    

  def indian_dish(self):
    dish_list = ["Samosa","Vadapav","Panipuri","Kachori","Aloo Tikki","Pakora",]
    for i, each in enumerate(dish_list):
      indian_menu = ttk.Button(text=each)
      indian_menu.grid(row=i+1,column=1)
    

  def milkshakes_juice(self):
    dish_list = ["Oreo Milkshake","Kitkat Milkshake","Chocolate Milkshake","Strawberry Milkshake"]
    for i, each in enumerate(dish_list):
      milkshake_juice_menu = ttk.Button(text=each)
      milkshake_juice_menu.grid(row=i+1,column=2)
    

  def hot_bev(self):
    dish_list = ["Tea☕","Coffee🍵"]
    for i, each in enumerate(dish_list):
      tea_coffee = ttk.Button(text=each)
      tea_coffee.grid(row=i+1,column=3)
    

  def juice(self):
    dish_list = ["Apple🍎","Orange🍊","Watermelon🍉","Pomegranate","Pineapple🍍","Mango🥭"]
    for i, each in enumerate(dish_list):
      juice_menu = ttk.Button(text=each)
      juice_menu.grid(row=i+1,column=4)
    self.mainloop()




      
    
