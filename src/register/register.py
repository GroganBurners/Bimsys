import cgi
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.webapp import template

class Customer (db.Model):
    cust_type = db.StringProperty()#Generated from a dropdown menu Gas service/Gas Repair/Oil Service/Oil Repair
    cust_date = db.DateProperty(auto_now_add=True)#if not provided automatically generated
    cust_first_name = db.StringProperty()
    cust_last_name = db.StringProperty()
    cust_email = db.StringProperty()
    cust_password = db.StringProperty()
    cust_address1 = db.StringProperty()
    cust_address2 = db.StringProperty()
    cust_address3 = db.StringProperty()
    cust_county = db.StringProperty()
    cust_geocode = db.StringProperty(default = '0.0,0.0')#automatically generated if available
    cust_phone = db.PhoneNumberProperty()
    cust_mobile_phone = db.PhoneNumberProperty()
    
    type_of_work = db.StringProperty() #Service/Install/Repair/Other
    next_service = db.DateProperty() #Date of next service due
    notes = db.StringProperty()
    
    o2 = db.FloatProperty(0)
    coppm = db.FloatProperty(0)
    co2percent = db.FloatProperty(0)
    flumeTemp = db.FloatProperty(0)
    efficiency = db.FloatProperty(0)
    xsair = db.FloatProperty(0)
    
    

class MainPage(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__))
        self.response.out.write(template.render(path+'/register.html',{}))
        
    def post(self):
        #When the user hits the button we want to query google maps and get their 
        #geocode address, we then want to save this geocode in the datastore
        
        #http://maps.google.com/maps/api/geocode/xml?address=2+Corduff%20Gardens+Blanchardstown+Ireland&sensor=false
        
        
        registerme = Customer()
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
        path = os.path.join(os.path.dirname(__file__))
        self.response.out.write(template.render(path+'/thankyou.html',{}))


def main():
    app = webapp.WSGIApplication([('.*',MainPage)], debug=True)
    run_wsgi_app(app)

if __name__ == "__main__":
    main()