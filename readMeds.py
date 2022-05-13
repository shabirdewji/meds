# This code reads the meds.csv and sets up the push safer
# checks to see if it is time to take meds
# run this python script using crontab
# Shabir. Apr 2022


import csv
import datetime
from urllib.parse import urlencode
from urllib.request import Request, urlopen


hour = datetime.datetime.now().hour
diff = 0

def doNotify(med):
    # print(' Time for ', a)
    message = "Time to take: "+med+"."
    sound = 45
    url = 'https://www.pushsafer.com/api'

    post_fields = {
	        "t" : 'MEDS TIME',
	        "m" : message,
	        "s" : 45,
	        "v" : 0,
	        "i" : 33,
	        "c" : '#FF0000',
	        "d" : 'a',
	        "u" : 'https://www.pushsafer.com',
	        "ut" : 'Open Pushsafer',
	        "k" : 'Wb9Gadr2yUf3bZbqjfP3',
	        "p" : '',
	        "p2" : '',
	        }

    request = Request(url, urlencode(post_fields).encode())
    json = urlopen(request).read().decode()
    print(json)
    return

with open('meds.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # print(f'\t{row[0]} {row[1]} {row[2]}')

            diff = int(row[1]) - hour
            # print('diff: ', diff)
            if diff == 0 :
                doNotify(row[0])
            line_count += 1