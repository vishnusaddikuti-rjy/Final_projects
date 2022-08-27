from datetime import datetime as dt
import random
import pandas

my_email = "saddikutivishnu2019@iiitkottayam.ac.in"
password = "ramahyma"

import smtplib
today=dt.now()
today_tuple=(today.month,today.day)

data=pandas.read_csv("birthdays.csv")

birthdays_dict={(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person=birthdays_dict[today_tuple]
    file_path=f"letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents=letter_file.read()
        contents=contents.replace("[Name]",birthday_person["name"])
    #establishing connection
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],
                        msg=f"Subject:Happy Birthday!\n\n{contents}")
    connection.close()








