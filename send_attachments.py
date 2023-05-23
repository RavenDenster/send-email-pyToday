import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from pyfiglet import Figlet
from tqdm import tqdm
from email import encoders
import mimetypes
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase

def send_email(text=None, template=None):
    sender = 'olegkashe@gmail.com'
    password = 'wcuqcqwxrxliqdse'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        with open(template, encoding='utf-8') as file:
            tempate = file.read()
    except IOError:
        # return "The template file doesnt found!"
        template = None

    try:
        server.login(sender, password)
        # msg = MIMEText(tempate, 'html')
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = sender
        msg['Subject'] = 'С днём рождения!'

        if text:
            msg.attach(MIMEText(text))
        if template:
            msg.attach(MIMEText(tempate, 'html'))

        print('Collecting...')
        for file in tqdm(os.listdir('attachments')):
            filename = os.path.basename(file)
            ftype, encoding = mimetypes.guess_type(file)
            file_type, subtype = ftype.split('/')

            if file_type == 'text':
                with open(f'attachments/{filename}', encoding='utf-8') as f:
                    filei = MIMEText(f.read())
            elif file_type == 'image':
                with open(f'attachments/{filename}', 'rb') as f:
                    filei = MIMEImage(f.read(), subtype)
            elif file_type == 'audio':
                with open(f'attachments/{filename}', 'rb') as f:
                    filei = MIMEAudio(f.read(), subtype)
            elif file_type == 'application':
                with open(f'attachments/{filename}', 'rb') as f:
                    filei = MIMEApplication(f.read(), subtype)
            else:
                with open(f'attachments/{filename}', 'rb') as f:
                    filei = MIMEBase(file_type, subtype)
                    filei.set_payload(f.read())
                    encoders.encode_base64(filei)

            filei.add_header('content-disposition', 'attachment', filename=filename)
            msg.attach(filei)

        print('Sending...')
        server.sendmail(sender, sender, msg.as_string())

        return 'The message was send successfully!'
    except Exception as _ex:
        return f'{_ex}\nCheck your login or password please!'

def main():
    font_text = Figlet(font='slant')
    print(font_text.renderText('SEND EMAIL'))
    text = input("Type your text or press enter: ")
    template = input('Type template name or press enter: ')
    print(send_email(text=text, template=template))

if __name__ == '__main__':
    main()