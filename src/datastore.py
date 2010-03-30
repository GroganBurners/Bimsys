# -*- coding: utf-8 -*-
# Copyright Grogan Burner Services Ltd. 2010
# Licensed under GPL v3 or higher

from google.appengine.ext import db

class Customer (db.Model):
    cust_id = db.IntegerProperty()#Unique ID
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
    
class pageNews(db.Model):
    news_heading = db.StringProperty
    news_body = db.StringProperty