from crontab import CronTab

cron = CronTab(user=True)

cron.remove_all()

job = cron.new('/usr/bin/env python3 /home/machine/Desktop/code/NeekoMySaves/saveBackup.py')

job.minute.every(5)

for item in cron:
    print(item)

cron.write()