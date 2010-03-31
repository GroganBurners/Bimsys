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

def processCSVtoDB():
	################################
	## READ IN VALUES FROM FILE
	################################
	
	# Open the file and apply CSV reader to it - will be upload field on AppEngine
	readFile  = open('OilService.csv', "rb")
	reader = csv.reader(readFile)
	
	# Start a dictionary of columns, where we will store all the CSV rows
	column = []
	
	rownum = 0
	for row in reader:
	    #print 'Enter for loop to assign values into lines' # debug line
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
	
	#print header[1] # debug line
	#print column[90][1] # debug line
	#new = column[20][1].split(' ') # debug line
	#print new[0] # debug line
	#print new[1] # debug line
	
	
	"""
	## ASSIGN VALUES INTO DATABASE
	"""
	
	
	#Reset at 0 before Iteration
	lineno = 0
	
	print 'Getting to for loop before assigning values to db' # debug
	#Loop through all records, assigning correct values to DB fields
	for lines in column:
		print 'Enter for loop to assign value to db' # debug line
		# Row 0 is header, so throw away
		if lineno == 0: 
			print 'Header not needed for database'
		elif lineno >= 1:
			# Test if the customer ID is unique, not in use (yet)
			#if (custid != row[0])
			cust_id = rownum
			cust_type = 'oil' #Oil or gas? No info
			cust_date = column[lineno][0]

			# Split up Name values into First Name, Last Name and assign to temp variable to put in Database
			splitnames = column[lineno][1].split(' ')
			cust_first_name = splitnames[0] 
			if(splitnames.length()=1):
				cust_last_name = splitnames[1]
			if(splitnames.length()>=2):
				cust_last_name = splitnames[1] + splitnames[1]
			# END Name splitting

			#Set Password to last name
			cust_password = 'Grogan' # deb#splitnames[1] 

			# TODO Sanitixe if not enough address lines
			splitaddr = column[lineno][2].split(' ')
			cust_address1 = splitaddr[0]
			if(splitaddr.length()=1):
				cust_address2 = splitaddr[1]
			elif(splitaddr.length()=2):
				cust_address2 = splitaddr[1]
				cust_address3 = splitaddr[2]
			elif(splitaddr.length()>2):
				cust_address2 = splitaddr[1]
				cust_address3 = splitaddr[2]
				cust_county = splitaddr[3]
			# END address splitting

			cust_geocode = '0.0,0.0' # Don't have info
			cust_phone = 0000000000 # Don't have info
			cust_mobile_phone = 0000000000 # Don't have info

			##########
			# Services
			##########
			type_of_work = column[lineno][3] #Service/Install/Repair/Other
			next_service = column[lineno][4] #Date of next service due
			notes = column[lineno][5]

			####################
			# Service Statistics
			####################
			o2 = column[lineno][6]
			coppm = column[lineno][7]
			co2percent = column[lineno][8]
			flumeTemp = column[lineno][9]
			efficiency = column[lineno][10]
			xsair = column[lineno][11]

			# Iterate after record is done
			lineno += 1
		lineno += 1
	# Close the file  
	print 'Closing file from reading'
	readFile.close()
	#processDBtoCSV() # debug
		
		
#####################
## Export DB to CSV - using CSV Writer Module
####################
def processDBtoCSV():
	# Open the file and apply CSV writer to it - will be download option on AppEngine
	writeFile  = open('Output.csv', "wb")
	writer = csv.writer(writeFile)
	
	#Start at 0 before Iteration
	rownum = 0
	row = 0
	
	#print 'Getting to for loop before writing file' # debug
	#Loop through all records, assigning correct values to DB fields
	for row in reader:
		print 'Getting in to for loop before writing file' # debug
		# Row 0 is header, so throw away
		if rownum == 0: 
			writeFile.writerow('cust_id', 'cust_type', 'cust_date', 'cust_first_name', 'cust_last_name', 'cust_password', 'cust_address', 
			'cust_address2', 'cust_address3', 'cust_county', 'cust_geocode', 'cust_phone', 'cust_mobile_phone', 'type_of_work',
			'next_service', 'notes', 'o2', 'coppm', 'co2percent', 'flumeTemp', 'efficiency', 'xsair')
			print 'Writing Header' # debug line
		elif rownum >= 1:
			writeFile.writerow(cust_id, cust_type, cust_date, cust_first_name, cust_last_name, cust_password, cust_address1, 
			cust_address2, cust_address3, cust_county, cust_geocode, cust_phone, cust_mobile_phone, type_of_work,
			next_service, notes, o2, coppm, co2percent, flumeTemp, efficiency, xsair)
			print 'Writing Customer Records' # debug line
			# Iterate after record is done
			rownum += 1
		rownum += 1
	# Close the file  
	writeFile.close()
	print 'Written output to CSV file'
	#readFile.close() # debug

if __name__ == "__main__":
    processCSVtoDB()
