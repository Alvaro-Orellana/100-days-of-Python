from smtplib import SMTP
from datetime import datetime
import random

email = "testforpythoncourse@gmail.com"
password = "kagf zprj ctit xjyw"
destination_email = "alvaro.hernan.orellana@gmail.com"

with open("quotes.txt") as quotes_file:
    weekday = datetime.now().strftime("%A")
    quote_of_the_day = random.choice(quotes_file.readlines())
    message = f"Here is your {weekday}'s quote!\n\n{quote_of_the_day}"

with SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(email, password)
    connection.sendmail(from_addr=email, to_addrs=destination_email, msg=message)


