import csv
from users.models import Institute
with open('INUNI.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        i = Institute.objects.create(name=row[0])
        i.save()

from users.models import City
with open('cl.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        c = City.objects.create(name=row[0], state=row[1])
        c.save()
