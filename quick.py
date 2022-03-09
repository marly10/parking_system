# Import modules
import smtplib, ssl
## email.mime subclasses
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
### Add new subclass for adding attachments
##############################################################
from email.mime.application import MIMEApplication
##############################################################



# Define a function to attach files as MIMEApplication to the email
##############################################################
def attach_file_to_email(email_message, filename):
    # Open the attachment file for reading in binary mode, and make it a MIMEApplication class
    with open(filename, "rb") as f:
        file_attachment = MIMEApplication(f.read())
    # Add header/name to the attachments    
    file_attachment.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    # Attach the file to the message
    email_message.attach(file_attachment)
##############################################################    

# Set up the email addresses and password. Please replace below with your email address and password
email_from = 'buildawebsite1010@gmail.com'
password = 'npxjcjnqcxfmwnmo'
email_to = 'rickymarly7@gmail.com'


# Create a MIMEMultipart class, and set up the From, To, Subject fields
email_message = MIMEMultipart()
email_message['From'] = email_from
email_message['To'] = email_to
email_message['Subject'] = 'Report email'


# Attach more (documents)
##############################################################
attach_file_to_email(email_message, 'example.ics')

##############################################################
# Convert it as a string
email_string = email_message.as_string()

# Connect to the Gmail SMTP server and Send Email

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.ehlo()
    server.login(email_from, password)
    server.sendmail(email_from, email_to, email_string)
    server.close()