##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

import smtplib, pandas, random, datetime as dt

def send_email(to_email:str, message:str):
    from_email = "testforpythoncourse@gmail.com"
    password = "kagf zprj ctit xjyw"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(from_email, password)
        connection.sendmail(from_email, to_email, message)

today = dt.datetime.today()
birthdays_table = pandas.read_csv('birthdays.csv')

for _, row in birthdays_table.iterrows():
    if (today.month, today.day) == (row.month, row.day):
        letter_file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
        with open(letter_file_path) as letter:
            message = letter.read().replace("[NAME]", row['name'])
            send_email(row.email, message)


