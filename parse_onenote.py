import sys
import csv
from datetime import datetime

path = sys.argv[1]
output = sys.argv[2]
entries = []

with open(path, 'r') as f:
    for line in f:

        # Get rid of question marks
        if line.strip() == '?':
            continue

        # Get rid of notebook headers
        try:
            date = datetime.strptime(line.strip(), '%B %Y')
            next(f)
            next(f)
            next(f)
            continue

        except ValueError as e:
            pass
            #  print(e)

        tmp = line.split(' ')[0]
        if tmp[-1] == ',' or tmp[-1] == ':':
            tmp = tmp[:-1]

        date = None
        try:
            date = datetime.strptime(tmp.strip(), '%m/%d/%y')
        except ValueError as e:
            pass

        try:
            date = datetime.strptime(tmp.strip(), '%m/%d/%Y')
        except ValueError as e:
            pass

        # entry[0] = date
        # entry[1] = text
        if date is None:
            entry[1] = entry[1] + '\n' + line
        else:
            try:
                entry[1] = entry[1].strip()
                entries.append(entry)
            except NameError as e:
                pass
            entry = [date, '']

with open(output, 'w') as out:
    writer = csv.writer(out, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(['Date', 'Text'])
    for entry in entries:
        writer.writerow(entry)
