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

import csv
from datetime import datetime
from users.models import School
with open('schools.csv') as f:
    reader = csv.reader(f)
    headers = next(reader)
    for row in reader:
        datestring = row[13]
        date = ''
        if datestring:
            dt = datetime.strptime(datestring, '%b %d, %Y')
            date = dt.date()
        c = School.objects.create(
            name=row[0],
            affiliation_no=row[1],
            state=row[2],
            distric=row[3],
            region=row[4],
            address=row[5],
            pincode=row[6],
            ph_no=str(row[7]),
            off_ph_no=str(row[8]),
            res_ph_no=str(row[9]),
            email=row[10],
            website=row[11],
            year_found=row[12],
            date_opened=date,
            principal_name=row[14],
            principal_qual=row[15],
            principal_exp_teach=row[16],
            principal_exp_adm=row[19],
            status=row[17],
            society_name=row[18]
        )
        c.save()
