import csv
from features import price, race
import random
import sys
from util import thorn_row

def main():
	out_file = sys.argv[1]
	f = open(out_file, "w")
	w = csv.writer(f)
	w.writerow(["City","Age","Date","Phone","Price","Race"])

	tr = thorn_row()
	samples = []

	for row in tr:
		if len(row)<13:
			continue
		if row[0] != "Backpage.com":
			continue
		title = row[3]
		text  = row[5]
		w.writerow([row[1],
			        row[4],
			        row[6],
			        row[10],
			        price(title, text),
			        race( title, text)])

	f.close()

if __name__=="__main__":
	main()
