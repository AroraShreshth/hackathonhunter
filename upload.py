from users.models import Skill, City, Institute
import csv
i = 0
with open('INUNI.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        i = Institute.objects.create(name=row[0])
        i.save()
        i = i+1
        print(i)

i = 0
with open('cl.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        c = City.objects.create(name=row[0], state=row[1])
        c.save()
        i = i+1
        print(i)


i = 0
with open('skills.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        s = Skill.objects.create(name=row[0])
        s.save()
        i = i+1
        print(i)
