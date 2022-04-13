from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def send_mail(subject, message, users):
    for i in users:
        msg = MIMEMultipart()
        msg["From"] = "anastasia.kim.mobile@gmail.com"
        msg["To"] = i.email
        msg["Subject"] = subject
        password = "ypdzgjmsrkdogkcg"

        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com: 587')

        server.starttls()
        server.login(msg["From"], password)
        server.sendmail(msg["From"], msg["To"], msg.as_string(()))

        server.quit()
        print('Your mail was sent')

