import csv
import math
from datetime import datetime
from users.models import School
i = 1
j = 0
with open('schools.csv') as f:
    reader = csv.reader(f)
    headers = next(reader)
    for row in reader:
        print(i)
        datestring = row[13]
        date = None
        exp_teach = None
        exp_adm = None

        if datestring:
            dt = datetime.strptime(datestring, '%b %d, %Y')
            date = dt.date()
        if row[16]:
            exp_teach = row[16]

        if row[19]:
            exp_adm = row[19]
        try:
            c = School.objects.create(
                name=row[0],
                affiliation_no=row[1],
                state=row[2],
                distric=row[3],
                region=row[4],
                address=row[5],
                pincode=row[6] if row[6] else None,
                ph_no=str(row[7]),
                off_ph_no=str(row[8]),
                res_ph_no=str(row[9]),
                email=row[10],
                website=row[11],
                year_found=row[12] if row[12] else None,
                date_opened=date,
                principal_name=row[14],
                principal_qual=row[15],
                principal_exp_teach=exp_teach,
                principal_exp_adm=exp_adm,
                status=row[17],
                society_name=row[18]
            )
            c.save()
            i += 1
        except Exception:
            print('this one didnt work ')
            j += 1

print(j)
