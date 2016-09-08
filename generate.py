import json
import csv
import os

# where is your locationhistory.json file located?
fname = '\path\to\locationhistory.json'

# read json file
print 'reading file'
file = open(fname, "r")
content = file.read()
file.close()

# read json
print 'loading json'
data = json.loads(content)

# create file
print 'creating csv'
fieldnames = ["Geometry"]
w = open('history.csv', 'wb')
wr = csv.writer(w, delimiter=',')
wr.writerow(fieldnames)

output = ""
count = len(data['locations'])
for c in xrange(0,count):
    row = data['locations'][c]

    if(round(row['longitudeE7'] / 10000000) != -122):
        output += str(float(row['longitudeE7']) / 10000000) + "," + str(float(row['latitudeE7']) / 10000000) + ",0.0 ";
	# merge every 10 000 coordinates into one line
    if((c % 10000 == 0 and c != 0) or c == count-1):
        wr.writerow(['<LineString><coordinates>' + output + '</LineString></coordinates>'])
        output = ""
w.close()
print 'finished'