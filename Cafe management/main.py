# from tkinter import *
# import time
# from all_fun import Menu


# window = Tk()
# window.title("cafe")
# window.minsize(height=600,width=600)
# window.config(width=600,height=600,padx=20,pady=20,bg="#F5D2D2")

# #Cafe Title
# heading = Label(
#   window,
#   text="🍔🥪//🥐🍩Pixel-Cafe🍪🧁//🍕🍟",
#   font=("Comic Sans MS",28,"normal"),
#   bg="#A3CCDA",
#   fg="#F8F7BA",
#   padx=10,
#   pady=10
#   )
# heading.grid(column=0,row=0,pady=20,columnspan=2)

# #menu
# menu = Label(
#   window,
#   text="What uhh like to have??",
#   bg="#F8F7BA",
#   font=("Comic Sans MS",20,"normal"),
#   fg="#F5D2D2")
# menu.grid(column=0,row=1,pady=10)
# #pizza
# pizza = Button(
#   text="Pizza🍕",
#   fg="white",
#   bg="#A3CCDA",
#   font=("Comic Sans MS",11,"normal"),
#   width=20,
#   command=m.on_click_menu())
# pizza.grid(column=0,row=2,pady=10)

# #Burger
# burger = Button(
#   text="Burger🍔",
#   fg="white",
#   bg="#A3CCDA",
#   font=("Comic Sans MS",11,"normal"),
#   width=20)
# burger.grid(column=0,row=3,pady=10)

# #pastry
# pastry = Button(
#   text="Pastry🍰",
#   fg="white",
#   bg="#A3CCDA",
#   font=("Comic Sans MS",11,"normal"),
#   width=20)
# pastry.grid(column=0,row=4,pady=10)

# #Pasta
# pasta = Button(
#   text="Pasta🍝",
#   fg="white",
#   bg="#A3CCDA",
#   font=("Comic Sans MS",11,"normal"),
#   width=20)
# pasta.grid(column=0,row=5,pady=10)

# #browine
# brownie = Button(
#   text="Brownie🍥",
#   fg="white",
#   bg="#A3CCDA",
#   font=("Comic Sans MS",11,"normal"),
#   width=20)
# brownie.grid(column=0,row=6,pady=10)

# #sandwich
# sandwich = Button(
#   text="Sandwich🥪",
#   fg="white",
#   bg="#A3CCDA",
#   font=("Comic Sans MS",11,"normal"),
#   width=20)
# sandwich.grid(column=0,row=7,pady=10)



# #asking bill
# ask_bill = Label(
#   window,
#   text="Shall I make ur bill??",
#   bg="#F8F7BA",
#   font=("Comic Sans MS",20,"normal"),
#   fg="#F5D2D2")
# ask_bill.grid(column=1,row=1,pady=10)


# #Yes or no
# yeah_sure = Button(
#   text="Yeahh Sure!!",
#   fg="white",
#   bg="#A3CCDA",
#   font=("Comic Sans MS",10,"normal"),
#   width=30)
# yeah_sure.grid(column=1,row=2,pady=10)

# #bill
# def give_bill():
#   bill = Label(window,text="Have a Nice Day!!\n😊😃😄😀🫠\n😋😋",
#                bg="#F8F7BA",
#     font=("Comic Sans MS",20,"normal"),
#     fg="#F5D2D2")
#   bill.grid(column=1,row=3,pady=10,rowspan=3)


# give_bill = window.after(5000,give_bill())




# window.mainloop()

# from tkinter import *
# from tkinter import ttk

# root = Tk()
# root.title("Cafe Order Table")
# root.geometry("600x400")
# root.config(bg="#F5D2D2")

# # Define columns for the Treeview
# columns = ("Item", "Qty", "Price", "Total")

# # Create Treeview widget
# order_table = ttk.Treeview(root, columns=columns, show="headings", height=8)

# # Define column headings
# order_table.heading("Item", text="Item")
# order_table.heading("Qty", text="Quantity")
# order_table.heading("Price", text="Price (₹)")
# order_table.heading("Total", text="Total (₹)")

# # Set column widths
# order_table.column("Item", width=150, anchor="center")
# order_table.column("Qty", width=80, anchor="center")
# order_table.column("Price", width=100, anchor="center")
# order_table.column("Total", width=100, anchor="center")

# # Add table to window
# order_table.pack(pady=20)

# # --- Example: Add items when button is clicked ---
# def add_item():
#     item = "Burger🍔"
#     qty = 2
#     price = 80
#     total = qty * price
#     order_table.insert("", "end", values=(item, qty, price, total))

# add_button = Button(root, text="Add Item", font=("Comic Sans MS", 12),
#                     bg="#A3CCDA", fg="white", command=add_item)
# add_button.pack(pady=10)

# root.mainloop()

# from tkinter import *
# from tkinter import ttk
# import pandas as pd

# root = Tk()
# root.title("Cafe Order Table")
# root.geometry("600x400")
# root.config(bg="#F5D2D2")

# # --- Load CSV ---
# menu_data = pd.read_csv("menu.csv")

# # --- Treeview Setup ---
# columns = ("Item", "Qty", "Price", "Total")
# order_table = ttk.Treeview(root, columns=columns, show="headings", height=8)
# for col in columns:
#     order_table.heading(col, text=col)
#     order_table.column(col, anchor="center", width=100)
# order_table.pack(pady=20)

# # --- Helper: Add item to Treeview ---
# def add_item(item_name):
#     # Find the item in CSV
#     item_row = menu_data.loc[menu_data["Item"] == item_name]

#     if not item_row.empty:
#         price = int(item_row["Price"].values[0])
#         qty = 1  # default add 1 each time clicked
#         total = qty * price

#         # Check if item already exists in TreeView
#         found = False
#         for child in order_table.get_children():
#             values = order_table.item(child)["values"]
#             if values[0] == item_name:
#                 # If already exists, update qty & total
#                 new_qty = values[1] + 1
#                 new_total = new_qty * price
#                 order_table.item(child, values=(item_name, new_qty, price, new_total))
#                 found = True
#                 break
        
#         # If not found, insert as new
#         if not found:
#             order_table.insert("", "end", values=(item_name, qty, price, total))

# # --- Example Buttons ---
# buttons_frame = Frame(root, bg="#F5D2D2")
# buttons_frame.pack(pady=10)

# for dish in menu_data["Item"]:
#     btn = Button(buttons_frame, text=dish, bg="#A3CCDA", fg="white", font=("Comic Sans MS", 12),
#                  command=lambda d=dish: add_item(d))
#     btn.pack(side=LEFT, padx=5, pady=5)

# # --- Bill Button ---
# def calculate_total():
#     total = 0
#     for child in order_table.get_children():
#         total += order_table.item(child)["values"][3]
#     print("Total Bill:", total)

# Button(root, text="Generate Bill", font=("Comic Sans MS", 12), bg="#F8F7BA", command=calculate_total).pack(pady=10)

# root.mainloop()


class MenuWindow(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Menu")
        self.minsize(width=600, height=600)
        self.config(bg="#F5D2D2", padx=20, pady=20)

        style = ttk.Style(self)
        style.configure("TButton", font=MENU_FONT)
        style.configure("TLabel", font=("Comic sans MS",28,"normal"),
                        foreground="#F8F7BA", background="#A3CCDA")

        self.menu_data = pd.read_csv("C:/tkinter projects/Cafe management/menu_list.csv")

        self.heading()
        self.create_treeview()
        self.western_buttons()
        self.indian_dish()
        self.milkshakes_juice()
        self.hot_bev()
        self.juice()

    def heading(self):
        pick = ttk.Label(self, text="Pick Whatever uhh wantt!!!")
        pick.grid(column=0, row=0, columnspan=5, pady=10)

    def create_treeview(self):
        columns = ("Item", "Qty", "Price", "Total")
        self.selected = ttk.Treeview(self, columns=columns, show="headings", height=8)
        for col in columns:
            self.selected.heading(col, text=col)
        self.selected.column("Item", width=150, anchor="center")
        self.selected.column("Qty", width=80, anchor="center")
        self.selected.column("Price", width=75, anchor="center")
        self.selected.column("Total", width=100, anchor="center")
        self.selected.grid(column=1, row=7, columnspan=3, rowspan=3)

    def add_item(self, item_name):
        item_row = self.menu_data.loc[self.menu_data["Item"] == item_name]
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
                    self.selected.item(child, values=(item_name, new_qty, price, new_total))
                    found = True
                    break
            if not found:
                self.selected.insert("", "end", values=(item_name, qty, price, total))

    def western_buttons(self):
        dish_list = ["Pizza🍕","Burger🍔","Sandwich🥪","Pasta🍝","Pastry🍰","Brownie🍥","Momos🥟","Waffle🧇","Donots🍩"]
        for i, each in enumerate(dish_list):
            btn = ttk.Button(self, text=each,
                             command=lambda e=each: self.add_item(e))
            btn.grid(row=i+1, column=0, padx=5, pady=7)

    # Repeat the same for other categories
    def indian_dish(self):
        dish_list = ["Samosa","Vadapav","Panipuri","Kachori","Aloo Tikki","Pakora"]
        for i, each in enumerate(dish_list):
            btn = ttk.Button(self, text=each,
                             command=lambda e=each: self.add_item(e))
            btn.grid(row=i+1, column=1)

    def milkshakes_juice(self):
        dish_list = ["Oreo Milkshake","Kitkat Milkshake","Chocolate Milkshake","Strawberry Milkshake"]
        for i, each in enumerate(dish_list):
            btn = ttk.Button(self, text=each,
                             command=lambda e=each: self.add_item(e))
            btn.grid(row=i+1, column=2)

    def hot_bev(self):
        dish_list = ["Tea☕","Coffee🍵"]
        for i, each in enumerate(dish_list):
            btn = ttk.Button(self, text=each,
                             command=lambda e=each: self.add_item(e))
            btn.grid(row=i+1, column=4)

    def juice(self):
        dish_list = ["Apple🍎","Orange🍊","Watermelon🍉","Pomegranate","Pineapple🍍","Mango🥭"]
        for i, each in enumerate(dish_list):
            btn = ttk.Button(self, text=each,
                             command=lambda e=each: self.add_item(e))
            btn.grid(row=i+1, column=3)

    def create_cancel_button(self):
    cancel_btn = ttk.Button(self, text="Cancel Selected Dish", command=self.cancel_item)
    cancel_btn.grid(column=1, row=11, columnspan=2, pady=10)

