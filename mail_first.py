#!/usr/bin/python3

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from icalendar import Calendar, Event, vCalAddress, vText
import pytz
from datetime import datetime
import os
from pathlib import Pathgg


cal = Calendar()
cal.add('attendee', 'MAILTO:rickymarly7@gmail.com')

event = Event()
event.add('summary', 'Python meeting about calendaring')
event.add('dtstart', datetime(2022, 10, 24, 8, 0, 0, tzinfo=pytz.utc))
event.add('dtend', datetime(2022, 10, 24, 10, 0, 0, tzinfo=pytz.utc))
event.add('dtstamp', datetime(2022, 10, 24, 0, 10, 0, tzinfo=pytz.utc))

organizer = vCalAddress('MAILTO:buildawebsite1010@gmail.com')
organizer.params['cn'] = vText('Sir Jon')
organizer.params['role'] = vText('CEO')
event['organizer'] = organizer
event['location'] = vText('London, UK')

# Adding events to calendar
cal.add_component(event)

directory = str(Path(__file__).parent.parent) + "/"
print("ics file will be generated at ", directory)
f = open(os.path.join(directory, 'example.ics'), 'wb')
f.write(cal.to_ical())
f.close()

body = '''2022-03-08'''

#The mail addresses and password
gmail_user = 'buildawebsite1010@gmail.com'
gmail_password = 'npxjcjnqcxfmwnmo'
to = ['rickymarly7@gmail.com']
subject = 'Lorem ipsum dolor sit amet'

sent_from = gmail_user

email_text = """\
From: %s
To: %s
Subject: %s


%s
""" % (sent_from, ", ".join(to), subject, body)

filename = "example.ics"

#Setup the MIMEa
try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)

# chmod u+x /Users/rickymarly/Desktop/vm_test/mail/gmail_two.py    
#auto execution: nohup /Users/rickymarly/Desktop/vm_test/mail/gmail_two.py &

