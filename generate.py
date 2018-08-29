import json
import csv
import os

# where is your locationhistory.json file located?
fname = 'path/to/locationhistory.json'

# read json file
print('reading file')
file = open(fname, "r")
content = file.read()
file.close()

# read json
print('loading json')
data = json.loads(content)

# create file
print('creating csv')
fieldnames = ["Geometry"]
w = open('history.csv', 'w')
wr = csv.writer(w, delimiter=',')
wr.writerow(fieldnames)

output = ""
outputCount = 0
count = len(data['locations'])

for c in range(0,count):

	# convert current location
	lon = float(data['locations'][c]['longitudeE7']) / 10000000
	lat = float(data['locations'][c]['latitudeE7']) / 10000000

	# get next location, except if this is the last of the list
	if c < count-1:
		nextLon = float(data['locations'][c+1]['longitudeE7']) / 10000000
		nextLat = float(data['locations'][c+1]['latitudeE7']) / 10000000
	else:
		nextLon = lon
		nextLat = lat

	output += str(lon) + "," + str(lat) + ",0.0 ";
	outputCount += 1


	# merge every 10 000 locations into one line or end the line if the next coordinate is too far away
	if((c % 10000 == 0 and c != 0) or c == count-1 or abs(nextLon - lon) > 0.25 or abs(nextLat - lat) > 0.25):
		# only save if this line has more than one coordinate
		if outputCount > 1:
			wr.writerow(['<LineString><coordinates>' + output + '</LineString></coordinates>'])
			output = ""
			outputCount = 0
			print('progress: ' + str(c) + '/' + str(count))
		else:
			output = ""
			outputCount = 0
			print('skipped coordinate: ' + str(lon) + ', ' + str(lat))


w.close()
print('finished')
