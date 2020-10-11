import csv
from datetime import datetime
with open('schools.csv') as f:
    reader = csv.reader(f)
    headers = next(reader)
    for row in reader:
        print(row[13], str(row[7]), str(row[8]), str(row[9]))
        datestring = row[13]
        if datestring:
            dt = datetime.strptime(datestring, '%b %d, %Y')
            print(dt.date())
