import smtplib

import random
import datetime as dt

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
  with open(file="C:/tkinter projects/Send Email/quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)



my_email = "sender_mail.com"
password = "app_password"

with smtplib.SMTP_SSL("smtp.gmail.com",465) as connection:
  connection.login(user=my_email,password=password)
  connection.sendmail(
    from_addr=my_email,
    to_addrs="reciever_mail@gmail.com",
    msg=quote"
   )