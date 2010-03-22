# Copyright Grogan Burner Services Ltd. 
# Written by Neil Grogan
# Licensed under GPL v3 or higher

import csv

f  = open('ServiceandRepair.csv', "rb")
reader = csv.reader(f)


dbfields = []
dbattributes = []

rownum = 0
for row in reader:
    # Save first line as Value headers
    if rownum == 0:
        header = row
    elif rownum >= 1:
         column = row
         #print '%-8s: %s' % (header[colnum], col)
         rownum += 1
    rownum += 1

print header[5]
print column[5][5]

f.close()