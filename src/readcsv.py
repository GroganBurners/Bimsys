# -*- coding: utf-8 -*-
# Copyright Grogan Burner Services Ltd. 2010
# Licensed under GPL v3 or higher

# TODO:
# Sanitize Address splits (try/catch?)
# Cater to both types of files (services and Repairs have different fields), Decide which type of Customer
# Write DB to CSV File

# Import database code
#import datastore
import csv
import cgi
import os

def readInCSVFile():
	# Open the file and apply CSV reader to it - will be upload field on AppEngine
	f  = open('OilService.csv', "rb")
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
	    	#Append each CSV record to List
	        column.append(row) 
	        # Iterate row number to process next record
	        rownum += 1
	        #print '%-8s: %s' % (header[colnum], col) # debug line
	    rownum += 1
	
	print header[1] # debug line
	print column[90][1] # debug line
	new = column[20][1].split(' ') # debug line
	print new[0]
	print new[1]
	
	# Call to process stored variables in Database
	# processCSVtoDB()
	
def processCSVtoDB():
	#Start at 0 before Iteration
	colno = 0
	
	#Loop through all records, assigning correct values to DB fields
	for row in reader:
		# Row 0 is header, so throw away
		if rownum == 0: 
			print 'Header not needed'
		elif rownum >= 1:
			# Test if the customer ID is unique, not in use (yet)
			#if (custid != row[0])
			cust_id = null
			cust_type = null #Oil or gas? No info
			cust_date = column[rownum][0]
			
			# Split up Name values into First Name, Last Name and assign to temp variable to put in Database
			splitnames = colnum[ruwnum][1].split(' ')
			cust_first_name = splitnames[0] 
			cust_last_name = splitnames[1]
			# END Name splitting
			
			#Set Password to last name
			cust_password = splitnames[1]
			
			# TODO Sanitixe if not enough address lines
			splitaddr = colnum[ruwnum][2].split(' ')
			cust_address1 = splitaddr[0]
			cust_address2 = splitaddr[1]
			cust_address3 = splitaddr[2]
			cust_county = splitaddr[3]
			# END address splitting
			
			cust_geocode = '0.0,0.0' # Don't have info
			cust_phone = null # Don't have info
			cust_mobile_phone = null # Don't have info
			
			##########
			# Services
			##########
			type_of_work = column[rownum][3] #Service/Install/Repair/Other
			next_service = column[rownum][4] #Date of next service due
    			notes = column[rownum][5]
    			
			####################
			# Service Statistics
			####################
			o2 = column[rownum][6]
    			coppm = column[rownum][7]
    			co2percent = column[rownum][8]
    			flumeTemp = column[rownum][9]
    			efficiency = column[rownum][10]
    			xsair = column[rownum][11]
			
			# Iterate after record is done
			colno += 1
		colno += 1
	# Close the file  
	f.close()
		
#####################
## Export DB to CSV - using CSV Writer Module
####################
def processDBtoCSV():
	# Open the file and apply CSV writer to it - will be download option on AppEngine
	f  = open('Output.csv', "rb")
	writer = csv.writer(f)
	
	#Start at 0 before Iteration
	colno = 0
	
	#Loop through all records, assigning correct values to DB fields
	for row in writer:
		# Row 0 is header, so throw away
		if rownum == 0: 
			f.writerow('cust_id', 'cust_type', 'cust_date', 'cust_first_name', 'cust_last_name', 'cust_password', 'cust_address', 
			'cust_address2', 'cust_address3', 'cust_county', 'cust_geocode', 'cust_phone', 'cust_mobile_phone', 'type_of_work',
			'next_service', 'notes', 'o2', 'coppm', 'co2percent', 'flumeTemp', 'efficiency', 'xsair')
		elif rownum >= 1:
			f.writerow(cust_id, cust_type, cust_date, cust_first_name, cust_last_name, cust_password, cust_address1, 
			cust_address2, cust_address3, cust_county, cust_geocode, cust_phone, cust_mobile_phone, type_of_work,
			next_service, notes, o2, coppm, co2percent, flumeTemp, efficiency, xsair)		
			# Iterate after record is done
			colno += 1
		colno += 1
	# Close the file  
	f.close()

if __name__ == "__main__":
    readInCSVFile()
