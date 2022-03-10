# Import modules
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

def attach_file_to_email(email_message, filename):
    
    with open(filename, "rb") as f:
        file_attachment = MIMEApplication(f.read())
    # Add header/name to the attachments    
    file_attachment.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    # Attach the file to the message
    email_message.attach(file_attachment)

    
def email_file_sender():
    # Set up the email addresses and password.#Please replace below with your email address and password
    email_from = 'buildawebsite1010@gmail.com'
    password = 'npxjcjnqcxfmwnmo'
    email_to = ['rickymarly7@gmail.com', 'tricianmckenzie@gmail.com']


    # Create a MIMEMultipart class, and set up the From, To, Subject fields
    email_message = MIMEMultipart()
    email_message['From'] = email_from
    email_message['To'] = ", ".join(email_to)
    email_message['Subject'] = 'Street Sweeping [AUTOMATION]'


    # Attach more (documents)
    ##############################################################
    
    dirname = '../calendar_invite/'
    
    # giving file extension
    ext = ('ics')
    
    # iterating over all files
    for files in os.listdir(dirname):
        if files.endswith(ext):
            attach_file_to_email(email_message, str(files))
            print(files)  # printing file name of desired extension
        else:
            print("not there")
            continue
    ##############################################################
    
    # Convert it as a string
    email_string = email_message.as_string()

    # Connect to the Gmail SMTP server and Send Email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.ehlo()
        server.login(email_from, password)
        server.sendmail(email_from, email_to, email_string)
        server.close()
        
email_file_sender()