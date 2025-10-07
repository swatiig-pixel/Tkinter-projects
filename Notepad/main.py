from tkinter import *

window = Tk()
window.title("My Notepad")
window.geometry("500x400")

def new_file():
    text_area.delete(1.0, END)


#Text input
text_area = Text(window,wrap="word",font=("Times New Roman",15,"normal"))
text_area.pack(expand=True, fill='both')

#Menu bar
menu_ = Menu(window)
#File
file = Menu(menu_,tearoff=0)
file.add_command(label="New",command=new_file)
file.add_command(label="Open")
file.add_command(label="Save")
file.add_separator()
file.add_command(label="Exit")
menu_.add_cascade(label="File")
#Edit
edit = Menu(menu_,tearoff=0)
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
menu_.add_cascade(label="Edit")


window.config(menu=menu_)
window.mainloop()