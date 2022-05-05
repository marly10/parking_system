import boto3

# Import modules
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
import datetime

now = datetime.datetime.now()
now_two = datetime.datetime.now()
duration = now - now_two
duration_in_s = duration.seconds / 60

#first method
def emailSend():
    #random variable
    #now = datetime.datetime.now()
    emailSend = None
    mail_content = 'Hey Ricky VM was been started at '+str(now.strftime("%Y-%m-%d %H:%M:%S"))
    
    sender_address = 'buildawebsite1010@gmail.com'
    sender_pass = 'npxjcjnqcxfmwnmo'
    receiver_address = ['rickymarly7@gmail.com']

    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address[0]
    message['Subject'] = 'Email Python - AWS VM is on'   #The subject line
    
    #The body and the attachments for the mailbfg
    message.attach(MIMEText(mail_content, 'plain'))

    #Create SMTP session for sending the mail
    try:
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')
        emailSend = True
    except:
        emailSend = False
        print ('Something went wrong...')

    if emailSend == True:
        print (emailSend)
        print('We good!')

    else:
        print (emailSend)
        print('We not good!')
        
emailSend()

region = 'us-east-1'
instances = ['i-0b0cbc388a00af29e']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))
