#!/usr/bin/python3
from email.policy import default
from icalendar import Calendar, Event, vCalAddress, vText
import pytz
from datetime import datetime
import os
from pathlib import Path
import calendar
 
#print(find_first_monday(2022, 3, 8)) def find_first_monday(year, month, day): 
def day_selector( day_date):
    
    c = calendar.Calendar(firstweekday=calendar.SUNDAY)
    monthcal = c.monthdatescalendar(datetime.today().year, datetime.today().month)
 
    try:
        
        if day_date == "MONDAY2":
            monday_second = [day for week in monthcal for day in week 
                             if day.weekday() == calendar.MONDAY and day.month== datetime.today().month][1]
            return monday_second
        
        elif day_date == "TUESDAY2":
            tuesday_second = [day for week in monthcal for day in week 
                              if day.weekday() == calendar.TUESDAY and day.month== datetime.today().month][1]
            return tuesday_second
        
        elif day_date == "MONDAY4":
            monday_fourth = [day for week in monthcal for day in week 
                             if day.weekday() == calendar.MONDAY and day.month== datetime.today().month][3]
            return monday_fourth
        
        elif day_date == "TUESDAY4":
            tuesday_fourth = [day for week in monthcal for day in week 
                              if day.weekday() == calendar.TUESDAY and day.month == datetime.today().month][3]
            return tuesday_fourth
        
        else: 
            print("Broken") 

    except IndexError:
        print('No date found')
        
    finally:
        print('This is always executed') 
        
print(day_selector("MONDAY2"))
print(day_selector("TUESDAY2"))
#print(day_selector("MONDAY4", 3))
#print(day_selector("TUESDAY4", 3))
     
#test print
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
f = open(os.path.join(directory, 'moveCar.ics'), 'wb')
f.write(cal.to_ical())
f.close()