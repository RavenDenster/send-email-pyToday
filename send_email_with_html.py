import smtplib
from email.mime.text import MIMEText

def send_email():
    sender = 'olegkashe@gmail.com'
    password = 'wcuqcqwxrxliqdse'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # text = """
    #     <!DOCTYPE html>
    #     <html lang="en">
    #     <head>
    #         <meta charset="UTF-8">
    #         <meta http-equiv="X-UA-Compatible" content="IE=edge">
    #         <meta name="viewport" content="width=device-width, initial-scale=1.0">
    #         <title>Document</title>
    #     </head>
    #     <body>
    #         <h1 style="color: green;">Привет!!!</h1>
    #         <span><u>Как у вас дела?<u/></span>
    #     </body>
    #     </html>
    # """

    try:
        with open('email_template.html') as file:
            tempate = file.read()
    except IOError:
        return "The template file doesnt found!"

    try:
        server.login(sender, password)
        msg = MIMEText(tempate, 'html')
        msg['From'] = sender
        msg['To'] = sender
        msg['Subject'] = 'С днём рождения!'
        server.sendmail(sender, sender, msg.as_string())

        return 'The message was send successfully!'
    except Exception as _ex:
        return f'{_ex}\nCheck your login or password please!'

def main():
    print(send_email())

if __name__ == '__main__':
    main()