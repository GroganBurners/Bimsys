#import cgi
import os
#We will use the app.yaml file to point toward this file for all requests
#We will then route requests from here.

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
#from google.appengine.ext import db
from google.appengine.ext.webapp import template


class MainPage(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path,{'sub1':'Substituted from Template'}))
        
class ber(webapp.RequestHandler):
    def get (self):
        path = os.path.join(os.path.dirname(__file__), '/html/ber.html')
        self.response.out.write(template.render(path,0))
        
class oil(webapp.RequestHandler):
    def get (self):
        path = os.path.join(os.path.dirname(__file__), 'html/oil.html')
        self.response.out.write(template.render(path,0))
        
class gas(webapp.RequestHandler):
    def get (self):
        path = os.path.join(os.path.dirname(__file__), 'html/gas.html')
        self.response.out.write(template.render(path,0))
        
class contact(webapp.RequestHandler):
    def get (self):
        path = os.path.join(os.path.dirname(__file__), 'html/contact.html')
        self.response.out.write(template.render(path,0))

application = webapp.WSGIApplication(
                                     [
                                      ('/', MainPage),
                                      ('/ber/', ber),
                                      ('/oil/', oil),
                                      ('/gas/', gas),
                                      ('/contact/', contact),
                                      ],debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()