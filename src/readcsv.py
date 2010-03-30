# -*- coding: utf-8 -*-
# Copyright Grogan Burner Services Ltd. 
# Written by Neil Grogan
# Licensed under GPL v3 or higher

# Import Mark's database code
import datastore
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
			#cust_id = column[rownum][0]
			#cust_type
			#cust_date
			## TODO Split strings after space
			#cust_first_name =
			#cust_last_name = 
			## END TODO
			#cust_password =
			#cust_address1 =
			#cust_address2 =
			#cust_address3 =
			#cust_county =
			#cust_geocode = '0.0,0.0'
			#cust_phone =
			#cust_mobile_phone =
			
			###########
			## Services
			###########
			#type_of_work = #Service/Install/Repair/Other
			#next_service = #Date of next service due
    			#notes = 
    			
			#####################
			## Service Statistics
			#####################
			#o2 = 
    			#coppm = 
    			#co2percent = 
    			#flumeTemp = 
    			#efficiency = 
    			#xsair = 		 
			## Debug printout
			#print column[colno][headerno]
	
			#colno++
		#headerno++

#####################
## Export DB to CSV
####################
def processCSVtoDB():



if __name__ == "__main__":
    readInCSVFile()
