#Imports Start
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
#Import DataStore modules
import datastore
#Import DataStore modules End

#Imports End
count = 0
customerList = datastore.Customer.all()

for i in customerList:
    count = count + 1

results = customerList.fetch(count)


class Admin(webapp.RequestHandler):
    def get(self):
        #Request the current size of the datastore module
        #storeSize = datastore.Customer.__sizeof__()
        #Assign the whole store to this variable
        #Get the whole datastore
        #template.render(path,{'results':results})
        path = os.path.join(os.path.dirname(__file__)+'/templates/admin/','base1Column.html')
        self.response.out.write(template.render(path,{'results':results}))
        
class oilService(webapp.RequestHandler):
    def get(self):
        customerList.filter('cust_type=', '1')#Filter the results according to the type of customer, then send the results.
        path = os.path.join(os.path.dirname(__file__)+'/templates/admin/','base1Column.html')
        self.response.out.write(template.render(path,{'results':results}))
        
class oilRepair(webapp.RequestHandler):
    def get(self):
        customerList.filter('cust_type=', '2')
        path = os.path.join(os.path.dirname(__file__)+'/templates/admin/','base1Column.html')
        self.response.out.write(template.render(path, {'results':results}))
        
class gasService(webapp.RequestHandler):
    def get(self):
        customerList.filter('cust_type=', '3')
        path = os.path.join(os.path.dirname(__file__)+'/templates/admin/','base1Column.html')
        self.response.out.write(template.render(path, {'results':results}))
        
class gasRepair(webapp.RequestHandler):
    def get(self):
        customerList.filter('cust_type=', '4')
        path = os.path.join(os.path.dirname(__file__)+'/templates/admin/','base1Column.html')
        self.request.out.write(template.render(path, {'results':results}))
        