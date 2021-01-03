import csv,sys,os
project_dir = "C:\wen\wen"
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = "wen.settings"
import django
django.setup()
from mainsite.models import company
data = csv.reader(open("C:\wen\wen\mainsite\data.csv",encoding="utf-8"),delimiter=",",)
for row in data:
    if row[0] !='time':
        unit = company()
        unit.time = row[0]
        unit.place = row[1]
        unit.people = row[2]
        unit.car = row[3]
        unit.longitude = row[4]
        unit.latitude = row[5]
        unit.save()