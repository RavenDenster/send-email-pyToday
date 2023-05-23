import smtplib
from email.mime.text import MIMEText

def send_email(message):
    sender = 'olegkashe@gmail.com'
    password = 'wcuqcqwxrxliqdse'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg['Subject'] = 'Click, slave!'
        server.sendmail(sender, sender, msg.as_string())

        # server.sendmail(sender, sender, f"Subject: Click me!\n{message}")

        return 'The message was send successfully!'
    except Exception as _ex:
        return f'{_ex}\nCheck your login or password please!'

def main():
    message = input('Type your message: ')
    print(send_email(message=message))

if __name__ == '__main__':
    main()