import calendar
from datetime import datetime
# Show every month
for month in range(1, 13):
    cal = calendar.monthcalendar(datetime.today().year, datetime.today().month)
    first_week  = cal[0]
    second_week = cal[1]
    third_week  = cal[2]
    forth_week  = cal[3]

    # If a Saturday presents in the first week, the second Saturday
    # is in the second week.  Otherwise, the second Saturday must 
    # be in the third week.
    
    if first_week[calendar.MONDAY]:
        holi_day = second_week[calendar.MONDAY]
    else:
        holi_day = third_week[calendar.MONDAY]

    print('%3s: %2s' % (calendar.month_abbr[month], holi_day))
    
    print(first_week[calendar.MONDAY])
    print(second_week[calendar.MONDAY])
    print(third_week[calendar.MONDAY])
    print(forth_week[calendar.MONDAY])
    
    print(first_week[calendar.TUESDAY])
    print(second_week[calendar.TUESDAY])
    print(third_week[calendar.TUESDAY])
    print(forth_week[calendar.TUESDAY])
    
print(int(datetime.today().year))