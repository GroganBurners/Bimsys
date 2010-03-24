# Copyright Grogan Burner Services Ltd. 
# Written by Neil Grogan
# Licensed under GPL v3 or higher

import csv
import cgi
import os
#from google.appengine.ext import webapp
#from google.appengine.ext.webapp.util import run_wsgi_app
#from google.appengine.ext import db
#from google.appengine.ext.webapp import template

def readInCSVFile():
	# Open the file and apply CSV reader to it
	f  = open('ServiceandRepair.csv', "rb")
	reader = csv.reader(f)
	
	# Start a dictionary of columns, where we will store all the CSV rows
	column = []
	
	rownum = 0
	for row in reader:
	    # Save first line as Value headers
	    if rownum == 0: 
	    	# Assign first row to be header (eg. Customer, Address, etc) 
	        header = row
	    elif rownum >= 1:
	    	#Append each CSV record to Dictionary
	        column.append(row) 
	        # Iterate row number to process next record
	        rownum += 1
	        #print '%-8s: %s' % (header[colnum], col) # debug line
	    rownum += 1
	
	print header[2] # debug line
	print column[90][2] # debug line
	
	# Call to process stored variables in Database
	# processCSVtoDB()
	
	# Close the file  
	f.close()
	
def processCSVtoDB():
	#headerno = 0
	#colno = 0
	#
	#for row in column
	#	header[headerno]
	#	for row in column
	#		print column[colno][headerno]
	#		colno++
	#	headerno++

	

if __name__ == "__main__":
    readInCSVFile()