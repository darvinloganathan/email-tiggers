import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import os

parent_dir="E:\\darvin\\etl_pro\\try4\\2021-11-15"

with open(parent_dir+'\\'+'result.txt','r') as f:
    lines = f.readlines()

s="".join(lines)

s

mail_content = s

#The mail addresses and password
sender_address = 'dar***************mail.com'
sender_pass = 'Da*******************47'
receiver_address = 'darvinloganathan@gmail.com'

#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'error log'
#The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))

files = [r'E:\darvin\etl_pro\try4\2021-11-15\result.zip']

for a_file in files:
    attachment = open(a_file, 'rb')
    file_name = os.path.basename(a_file)
    part = MIMEBase('application','octet-stream')
    part.set_payload(attachment.read())
    part.add_header('Content-Disposition',
                    'attachment',
                    filename=file_name)
    encoders.encode_base64(part)
    message.attach(part)

#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')