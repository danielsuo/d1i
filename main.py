import os
import sys
import csv

path = sys.argv[1]
lat = sys.argv[2]
lon = sys.argv[3]

with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile)
    headers = reader.next()
    for row in reader:
        cmd = 'dayone2 new "%(entry)s" --date="%(date)s --coordinate %(lat)s %(lon)s"' % \
            {
                'entry': row[1],
                'date': row[0],
                'lat': lat,
                'lon': lon
            }
        print(cmd)
        os.system(cmd)
