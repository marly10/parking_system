#!/usr/bin/python3
from email.policy import default
from icalendar import Calendar, Event, vCalAddress, vText, Alarm
import pytz
from datetime import datetime, date, timedelta
import os
from pathlib import Path
import calendar

#print(find_first_monday(2022, 3, 8)) def find_first_monday(year, month, day): 
def day_selector( day_date, variable_name):
    
 for month in range(1, 13):
        cal = calendar.monthcalendar(datetime.today().year, datetime.today().month)
        first_week  = cal[0]
        second_week = cal[1]
        third_week  = cal[2]
        forth_week  = cal[3]
        
        try:
            #2nd monday and tuesday of the month
            if day_date == "MONDAY2":
                    variable_name = second_week[calendar.MONDAY]
                    return variable_name
                
            elif day_date == "TUESDAY2":
                    variable_name = second_week[calendar.TUESDAY]
                    return variable_name
                
                #4th monday and tuesday of the month
            elif day_date == "MONDAY4":
                    variable_name = forth_week[calendar.MONDAY]
                    return variable_name
                
            elif day_date == "TUESDAY4":
                    variable_name = forth_week[calendar.TUESDAY]
                    return variable_name
            
            else: 
                print("Broken") 

        except IndexError:
            print('No date found')
            
        finally:
            print('This is always executed') 

#testing  
#file1 = day_selector("MONDAY2", "monday_second")
#file2 = day_selector("TUESDAY2", "tuesday_second")
#file3 = day_selector("MONDAY4", "monday_forth")
#file4 = day_selector("TUESDAY2", "tuesday_monday_forth")
#print("2nd MONDAY: "+str(file1))
#print("2nd TUESDAY: "+str(file2))
#print("4th MONDAY: "+str(file3))
#print("4th TUESDAY: "+str(file4))
    
def create_calendar(calendar_name, date):
        
    cal = Calendar()
    cal.add('attendee', 'MAILTO:rickymarly7@gmail.com')

    # need to type cast the year, month and day as variables
    event = Event()
    event.add('summary', 'Street sweeping - Move Car')
    event.add('dtstart', datetime(datetime.today().year, datetime.today().month, date, 15, 8, 0, tzinfo=pytz.utc))
    event.add('dtend', datetime(datetime.today().year, datetime.today().month, date, 15, 8, 0, tzinfo=pytz.utc))
    event.add('dtstamp', datetime(datetime.today().year, datetime.today().month, date, 0, 10, 0, tzinfo=pytz.utc))

    organizer = vCalAddress('MAILTO:buildawebsite1010@gmail.com')
    organizer.params['cn'] = vText('Ricky Batman')
    organizer.params['role'] = vText('Car Owner')
    event['organizer'] = organizer
    event['location'] = vText('San Diego, CA')
    
    #alarm1
    alarmtime1 = timedelta(minutes=-int(1440))
    icalalarm1 = Alarm()
    icalalarm1.add('action','DISPLAY')
    icalalarm1.add('trigger',alarmtime1)
    event.add_component(icalalarm1)
    
    #alarm2
    alarmtime2 = timedelta(minutes=-int(800))
    icalalarm2 = Alarm()
    icalalarm2.add('action','DISPLAY')
    icalalarm2.add('trigger',alarmtime2)
    event.add_component(icalalarm2)

    # Adding events to calendar
    cal.add_component(event)
    
    
    cwd = os.getcwd()
    folder_path = '../python_calendar'

    
    #makes calendar_folder
    if not os.path.exists('../calendar_invite'):
        os.makedirs('../calendar_invite')

    directory = "../calendar_invite"
    print("ics file will be generated at ", directory)
    f = open(calendar_name+'.ics', 'wb')
    f.write(cal.to_ical())
    f.close()

#calling function that makes/gets the right dates
m2 = day_selector("MONDAY2", "monday_second")
t2 = day_selector("TUESDAY2", "tuesday_second")
m4 = day_selector("MONDAY4", "monday_forth")
t4 = day_selector("TUESDAY4", "tuesday_forth")

#creates 4 calendar_invites
create_calendar("2nd_monday", m2)
create_calendar("2nd_tuesday", t2)
create_calendar("4th_monday", m4)
create_calendar("4th_tuesday", t4)
