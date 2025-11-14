import smtplib, schedule, time, random

# Estos son los que cambian como quieran
email_destino="alvaro.hernan.orellana@gmail.com"
mensaje="Vicencio y la concha de tu puta hermana " * random.randint(1, 33)
email_origen = "testforpythoncourse@gmail.com"
contraseña = "kagf zprj ctit xjyw"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(email_origen, contraseña)
    schedule.every(1).day.do(connection.sendmail, email_origen, email_destino, mensaje)

    while True:
        schedule.run_pending()
        time.sleep(60*60*24)