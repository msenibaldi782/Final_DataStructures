# -*- coding: utf-8 -*-
"""
Bus Tracker Suitcase

Created on Sat Jun  25 11:10:55 2020

@author: Matt Senibaldi

This program is designed to track the Chicago Busses

"""
import webbrowser
import urllib.request as ur

u = ur.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22') #Calling the bus tracking API
data = u.read() #reading the tracking data into varible data
f = open('rt22.xml', 'wb')      #Opening the XML file in the test folder to write any information pulled from the url
f.write(data)       #Writing the data into file f
f.close()           #Closing out the file once done writing data
print('Wrote rt22.xml')     #Telling the User the file has been written in the CMD line

from xml.etree.ElementTree import parse  
doc = parse('rt22.xml')

for bus in doc.findall('bus'):
    d=bus.findtext('d')
    lat = float(bus.findtext('lat'))
    
#webbrowser.open('https://www.google.com/maps/search/?api=1&parameters')
#webbrowser.open('https://developers.google.com/maps/documentation/staticmaps/')
webbrowser.open('https://www.google.com/maps/search/Chicago+rt+22/@41.980262,-87.668452,9.83z')
bus = {
       'id' : '6451',
       'lat' : 41.980262,
       'lon' : -87.668452
       }
print("Enter bus['lat'] for lattitude bus['lon'] for longitude bus['id'] for the ID")




    
        




