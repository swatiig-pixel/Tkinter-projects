from tkinter import *
from tkinter import ttk
import pandas as pd

MENU_FONT = ("Comic Sans MS",11,"normal")


class MenuWindow(Toplevel):

  def __init__(self,master=None):
    super().__init__(master)
    self.title("Menu")
    self.minsize(width=600,height=600)
    self.config(bg="#F5D2D2",padx=20,pady=20)

    style = ttk.Style(self)
    style.configure("TButton",
                    font=MENU_FONT,)
    style.configure("TLabel",
                    font=("Comic sans MS",28,"normal"),
                    foreground="#F8F7BA",
                    background="#A3CCDA")
    
    self.menu_data = pd.read_csv("C:/tkinter projects/Cafe management/menu_list.csv")
    self.heading()
    self.list_of_selected()
    self.cancel_button()
    self.western_buttons()
    self.indian_dish()
    self.milkshakes_juice()
    self.hot_bev()
    self.juice()
    self.list_of_selected()

    
  def heading(self):
    pick = ttk.Label(self,text="Pick Whatever uhh wantt!!!",font=("Comic Sans MS",28,"normal"),)
    pick.grid(column=0,row=0,columnspan=5,pady=10)


  def list_of_selected(self):
    columns= ("Item","Qty","Price","Total")
    self.selected = ttk.Treeview(self,columns=columns,show="headings",height=8)
    for col in columns:
      self.selected.heading(col,text=col)

    self.selected.column("Item",width=150,anchor="center")
    self.selected.column("Qty",width=80,anchor="center")
    self.selected.column("Price",width=75,anchor="center")
    self.selected.column("Total",width=100,anchor="center")

    self.selected.grid(column=1,row=7,columnspan=3,rowspan=3)

  def add_item(self,item_name):
    item_row = self.menu_data.loc[self.menu_data["Item"]==item_name]

    if not item_row.empty:
      price = int(item_row["Price"].values[0])
      qty = 1  
      total = qty * price

      found = False
      for child in self.selected.get_children():
        values = self.selected.item(child)["values"]
        if values[0] == item_name:
          new_qty = values[1] + 1
          new_total = new_qty * price
          self.selected.item(child,values=(item_name,new_qty,price,new_total))
          found = True
          break

      if not found:
        self.selected.insert("","end",values=(item_name,qty,price,total))

  def cancel_button(self):
    cancel_btn = ttk.Button(self,text="Cancel Selected Dish",command=self.cancel_item)
    cancel_btn.grid(column=1,row=11,columnspan=2,pady=10)

  def cancel_item(self,item_name):
    for child in self.selected.get_children():
            values = self.selected.item(child)["values"]
            if values[0] == item_name:
                if values[1] > 1:
                    new_qty = values[1] - 1
                    new_total = new_qty * values[2]
                    self.selected.item(child, values=(item_name, new_qty, values[2], new_total))
                else:
                    self.selected.delete(child)
                break
    




  def western_buttons(self):
    dish_list = ["Pizza🍕","Burger🍔","Sandwich🥪","Pasta🍝","Pastry🍰","Brownie🍥","Momos🥟","Waffle🧇","Donots🍩"]
    for i,each in enumerate(dish_list):
      west_menu = (ttk.Button(self,text=each,style="Custom.TButton",command=lambda e =each:self.add_item(e) ))
      west_menu.grid(row=i+1,column=0,padx=5,pady=7)
    

  def indian_dish(self):
    dish_list = ["Samosa","Vadapav","Panipuri","Kachori","Aloo Tikki","Pakora",]
    for i, each in enumerate(dish_list):
      indian_menu = ttk.Button(self,text=each,command=lambda e =each:self.add_item(e))
      indian_menu.grid(row=i+1,column=1)
    

  def milkshakes_juice(self):
    dish_list = ["Oreo Milkshake","Kitkat Milkshake","Chocolate Milkshake","Strawberry Milkshake"]
    for i, each in enumerate(dish_list):
      milkshake_juice_menu = ttk.Button(self,text=each,command=lambda e =each:self.add_item(e))
      milkshake_juice_menu.grid(row=i+1,column=2)
    

  def hot_bev(self):
    dish_list = ["Tea☕","Coffee🍵"]
    for i, each in enumerate(dish_list):
      tea_coffee = ttk.Button(self,text=each,command=lambda e =each:self.add_item(e))
      tea_coffee.grid(row=i+1,column=4)
    

  def juice(self):
    dish_list = ["Apple🍎","Orange🍊","Watermelon🍉","Pomegranate","Pineapple🍍","Mango🥭"]
    for i, each in enumerate(dish_list):
      juice_menu = ttk.Button(self,text=each,command=lambda e =each:self.add_item(e))
      juice_menu.grid(row=i+1,column=3)
    

  


  
    





      
    
