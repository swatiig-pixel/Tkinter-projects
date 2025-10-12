import smtplib

my_email = "arcane.lifestyle09.gmail.com"
password = "gfhm sqmm yvyd vetq"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs="swatiig1903@gmail.com",msg="Hello")
