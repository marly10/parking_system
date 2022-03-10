from crontab import CronTab

cron = CronTab(user='root')
job = cron.new(command='python write_test.py',  comment='comment')
job.minute.every(1)
for item in cron:
    print (item)

cron.write()
