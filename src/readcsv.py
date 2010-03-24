# Copyright Grogan Burner Services Ltd. 
# Written by Neil Grogan
# Licensed under GPL v3 or higher

import csv

f  = open('ServiceandRepair.csv', "rb")
reader = csv.reader(f)


column = []

rownum = 0
for row in reader:
    # Save first line as Value headers
    if rownum == 0:
        header = row
    elif rownum >= 1:
         column += row
         rownum += 1
         #print '%-8s: %s' % (header[colnum], col)
    rownum += 1

print header[2]
print column[2][2]

f.close()
