import calendar
from datetime import datetime
 
#print(find_first_monday(2022, 3, 8)) def find_first_monday(year, month, day):
 
c = calendar.Calendar(firstweekday=calendar.SUNDAY)
monthcal = c.monthdatescalendar(datetime.today().year, datetime.today().month)
 
try:
  #selects the 2nd monday& tuesdayof each month
  monday_second = [day for week in monthcal for day in week if day.weekday() == calendar.MONDAY and day.month== datetime.today().month][1]
  tuesday_second = [day for week in monthcal for day in week if day.weekday() == calendar.TUESDAY and day.month== datetime.today().month][1]
  
  #selects the 4nd monday& tuesdayof each month
  monday_fourth = [day for week in monthcal for day in week if day.weekday() == calendar.MONDAY and day.month== datetime.today().month][3]
  tuesday_fourth= [day for week in monthcal for day in week if day.weekday() == calendar.TUESDAY and day.month== datetime.today().month][3]

  
  #test print
  print(monday_second)
  print(tuesday_second)
  print(monday_fourth)
  print(tuesday_fourth)

except IndexError:
  print('No date found')
  
  #python3 -m venv my_env 
  #source my_env/bin/activate 
  #pip install -r requirements.txt