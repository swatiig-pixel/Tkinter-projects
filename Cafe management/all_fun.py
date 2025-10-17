from tkinter import *

class Menu(Tk):

  def on_click_menu(x):
    new_window = Toplevel(x)
    new_window.minsize(height=600,width=600)
