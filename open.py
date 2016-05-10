import csv
import json

filename = "RC_2015-05"
f = open(filename)
resultFile = open("May2015.csv",'w')
wr = csv.writer(resultFile, dialect='excel')
for line in f:
	info = json.loads(line)
	written = []
	if info.get('gilded') == 1:
		written.append(info.get('gilded'))
		written.append(info.get("subreddit"))
		written.append((info.get('score')))
		written.append((info.get('body')))
		wr.writerow(written)
f.close()
resultFile.close()
