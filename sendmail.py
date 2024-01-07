# from email.message import EmailMessage
# import ssl 
# import smtplib


# email_sender = 'deamon0x0@gmail.com'
# email_password = 'password'

# email_receiver = input("Email_Receiver: ")

# subject = input(""" Enter Subject: """)
# body = input("""Enter body of message: """)

# email = EmailMessage()
# email['From'] = email_sender
# email['To'] = email_receiver
# email['subject'] = subject
# email.set_content(body)

# context = ssl.create_default_context()

# with smtplib.SMTP_SSL('stmp.gmail.com', 465, context=context) as smtp:
#     smtp.login(email_sender, email_password)
#     smtp.sendmail(email_sender, email_receiver, email.as_string())




from email.message import EmailMessage
import smtplib, ssl

email_sender = 'deamon0x0@gmail.com'
email_receiver = input('Enter receiver mail: ')
email_password = input("Enter password: ")
email_subject = input("Enter subject: ")
email_body = input(""" Enter body of mail """)

email = EmailMessage()

email['From'] = email_sender
email['To'] = email_receiver
email['subject'] = email_subject
email.set_content(email_body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp@gmail.com', 465, context=context) as server:
    server.login(email_sender, email_password)
    server.sendmail(email_sender, email_receiver, email.as_string())

