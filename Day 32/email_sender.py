import smtplib
import schedule

# Estos son los que cambian como quieran
email_destino="alvaro.hernan.orellana@gmail.com"
mensaje="Vicencio y la concha de tu puta hermana " * 1000
numero_de_emails_a_enviar=5

# Estos no los cambian
email_origen = "testforpythoncourse@gmail.com"
contraseña = "kagf zprj ctit xjyw"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(email_origen, contraseña)

    schedule.every(numero_de_emails_a_enviar).second.do(
        lambda : connection.sendmail(email_origen, email_destino, mensaje)
    )
    schedule.run_pending()