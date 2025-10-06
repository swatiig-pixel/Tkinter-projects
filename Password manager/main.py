from tkinter import *
from tkinter import messagebox
import random

def generate_pass():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


  password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
  password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
  password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

  password_list = password_letters + password_symbols + password_numbers

  random.shuffle(password_list)

  passwordu = "".join(password_list)
  password_input.insert(0,passwordu)




def save():
  web = web_input.get()
  gmail = email_input.get()
  passwordz = password_input.get()

  if len(web) == 0 or len(passwordz) == 0:
    alert = messagebox.showinfo(title="Oops",message="You left some fields empty")
  else:
    is_ok = messagebox.askokcancel(title=web,message=f"These are the details entered:\nEmail: {gmail} \nPassword: {passwordz} \nIs it ok to save?")

    if is_ok:
      with open("data.txt","a") as data_file:
        data_file.write(f"{web} | {gmail} | {passwordz}\n")
        web_input.delete(0,END)
        password_input.delete(0,END)

  




window = Tk()
window.title("Password manager")
window.config(padx=40,pady=40)
window.minsize(200,200)

#Image
canvas = Canvas(window,width=200,height=200)
canvas.grid(column=1,row=0)
image_ = PhotoImage(file="C:/tkinter projects/Password manager/logo.png")
canvas.create_image(100,100,image=image_)

#website Label
website = Label(text="Website:")
website.grid(column=0,row=1)

#Email Label
email = Label(text="Email/Username:")
email.grid(row=2,column=0)

#Password Label
password = Label(text="Password:")
password.grid(row=3,column=0)

#Website entry
web_input = Entry(width= 45)
web_input.grid(column=1,row=1,columnspan=2)
web_input.focus()

#Email entry
email_input = Entry(width=45)
email_input.grid(column=1,row=2,columnspan=2)
email_input.insert(0,"swatiig1903@gmail.com")

#Password entry
password_input = Entry(width=21)
password_input.grid(column=1,row=3)

#label generate 
generate_pass = Button(text="Generate Password",command=generate_pass)
generate_pass.grid(column=2,row=3)

#Add button
add_button = Button(text="Add",width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()