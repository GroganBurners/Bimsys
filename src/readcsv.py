# -*- coding: utf-8 -*-
# Copyright Grogan Burner Services Ltd. 
# Written by Neil Grogan
# Licensed under GPL v3 or higher

# Import Mark's database code
#import datastore
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
	
	print header[6] # debug line
	print column[90][6] # debug line
	
	# Call to process stored variables in Database
	# processCSVtoDB()
	
	# Close the file  
	f.close()
	
#def processCSVtoDB():
	#Start at 0 before Iteration
	#headerno = 0
	#colno = 0
	
	#Loop through all records, assigning correct values to DB fields
	#for row in column
		## Row 0 is header, so throw away
		#if rownum == 0: 
			##discard
		#elif rownum >= 1:
			## Test if the customer ID is unique, not in use (yet)
			##if (custid != row[0])
			#cust_id = column[rownum][]
			#cust_type = column[rownum][] #Oil or gas? No info
			#cust_date = column[rownum][0]
			
			## TODO Split strings after space
			#cust_first_name = column[rownum][1] 
			#cust_last_name = column[rownum][1]
			## END TODO
			
			##Set Password to phone number
			#cust_password = null # Don't have info
			
			## TODO Split strings after space
			#cust_address1 = column[rownum][2]
			#cust_address2 = column[rownum][2]
			#cust_address3 = column[rownum][2]
			#cust_county = column[rownum][2]
			## END TODO
			
			#cust_geocode = '0.0,0.0' # Don't have info
			#cust_phone = null # Don't have info
			#cust_mobile_phone = null # Don't have info
			
			###########
			## Services
			###########
			#type_of_work = column[rownum][3] #Service/Install/Repair/Other
			#next_service = column[rownum][4] #Date of next service due
    			#notes = column[rownum][5]
    			
			#####################
			## Service Statistics
			#####################
			#o2 = column[rownum][6]
    			#coppm = column[rownum][7]
    			#co2percent = column[rownum][8]
    			#flumeTemp = column[rownum][9]
    			#efficiency = column[rownum][10]
    			#xsair = column[rownum][11]
		 
			## Debug printout
			#print column[colno][headerno]
	
			#colno+= 1

#####################
## Export DB to CSV - using CSV Writer Module
####################
#def processCSVtoDB():

if __name__ == "__main__":
    readInCSVFile()
