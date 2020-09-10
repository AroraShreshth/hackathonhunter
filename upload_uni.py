import csv
from users.models import Institute
with open('INUNI.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        i = Institute.objects.create(name=row[0])
        i.save()
