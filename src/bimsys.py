#import cgi
import os
#We will use the app.yaml file to point toward this file for all requests
#We will then route requests from here.

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
#from google.appengine.ext import db
from google.appengine.ext.webapp import template
import datastore
import admin
#class Customer(db.Model):
    #cust_email = db.StringProperty()
    #cust_password = db.StringProperty()
class MainPage(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__)+'/templates/','base.html')
        self.response.out.write(template.render(path,{}))
class Oil(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__)+'/templates/','oil.html')
        self.response.out.write(template.render(path,{}))
class Ber(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__)+'/templates/','ber.html')
        self.response.out.write(template.render(path,{}))
class Gas(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__)+'/templates/','gas.html')
        self.response.out.write(template.render(path,{}))
class Contact(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__)+'/templates/','contact.html')
        self.response.out.write(template.render(path,{}))
class Signin(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__)+'/templates/','signin.html')
        self.response.out.write(template.render(path,{}))
    def post(self):
        #GQL query to retrieve username and password from the datastore
        #Save query results in variables
        #Check variables against values from form
        #Forward user to Customer Dashboard if passwords match
        #Forward user to password retrieval page if passwords are incorrect
        #checkUser(self.request.get('email'))
        thisEmail = self.request.get('email')
        userPassword = datastore.Customer.all()
        userPassword.filter("cust_email =", thisEmail)
        
        results = userPassword.fetch(1)
        thisPassword = "gonnaChange"
        
        for p in results:
            thisPassword = p.cust_password
        
        if self.request.get('password') == thisPassword:
            path = os.path.join(os.path.dirname(__file__)+'/templates/','userDashboard.html')
            
        elif self.request.get('password') != thisPassword:
            path = os.path.join(os.path.dirname(__file__)+'/templates/','tryAgain.html')
        
        self.response.out.write(template.render(path,{}))

           
class customerDetails(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__)+'/templates/admin/','customerDetails.html')
        self.response.out.write(template.render(path,{}))
        #Need to block access...
            
class Register(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__)+'/templates/','register.html')
        self.response.out.write(template.render(path,{}))
    #When the user hits the button we want to query google maps and get their 
        #geocode address, we then want to save this geocode in the datastore
        
        #http://maps.google.com/maps/api/geocode/xml?address=2+Corduff%20Gardens+Blanchardstown+Ireland&sensor=false
   
    def post(self):        
        registerme = datastore.Customer()
        registerme.cust_id = registerme.__sizeof__()+1
        registerme.cust_first_name = self.request.get('first_name')
        registerme.cust_last_name = self.request.get('last_name')
        registerme.cust_email = self.request.get('email')
        registerme.cust_password = self.request.get('password')
        registerme.cust_address1 = self.request.get('address1')
        registerme.cust_address2 = self.request.get('address2')
        registerme.cust_address3 = self.request.get('address3')
        registerme.cust_county = self.request.get('county')
        registerme.cust_phone = self.request.get('phone')
        registerme.cust_mobile_phone = self.request.get('mobile_phone')
        
        registerme.put()#Place these values into the datastore
        path = os.path.join(os.path.dirname(__file__)+'/templates/','thankyou.html')
        self.response.out.write(template.render(path,{}))
        
def main():
    app = webapp.WSGIApplication([
                                  ('.signin.html',Signin),
                                  ('.oil.html',Oil),
                                  ('.ber.html',Ber),
                                  ('.gas.html',Gas),
                                  ('.contact.html',Contact),
                                  ('.register.html',Register),
                                  ('.customerDetails.html',customerDetails),
                                  ('.admin.html',admin.Admin),
                                  ('.oilService.html',admin.oilService),
                                  ('.oilRepair.html',admin.oilRepair),
                                  ('.gasService.html',admin.gasService),
                                  ('.gasRepair.html',admin.gasRepair),
                                  
                                  
                                  
                                  ('.*',MainPage)
                                  ], debug=True)
    run_wsgi_app(app)

if __name__ == "__main__":
    main()