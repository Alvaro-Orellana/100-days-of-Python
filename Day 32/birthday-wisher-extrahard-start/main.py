import csv  ##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas as pd
import random
import smtplib

def send_email(to_email:str, message:str):
    FROM_EMAIL = "testforpythoncourse@gmail.com"
    PASSWORD = "kagf zprj ctit xjyw"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(FROM_EMAIL, PASSWORD)
        connection.sendmail(FROM_EMAIL, to_email, message)

today = dt.datetime.today()
birthdays_table = pd.read_csv('birthdays.csv')

for _, row in birthdays_table.iterrows():
    if (today.month, today.day) == (row.month, row.day):
        letter_file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(letter_file_path) as letter:
            message = letter.read().replace("[NAME]", row['name'])
            send_email(row.email, message)


