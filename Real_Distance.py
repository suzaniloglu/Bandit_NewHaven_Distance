'''
Created on May 28, 2020

@author: si272
'''

'''
Created on Nov 7, 2019

@author: si272
'''
import csv
import json
import requests
from numpy import loadtxt
import xlrd
import pandas as pd


######################################## READ FILES ##############################
# FQHS locations excluded kids clinics
#F_Ohio = csv.DictReader(open("/Users/si272/Documents/LiClipse Workspace/FQHS_OTP_LOC_OHIO/Location_coverage_model/FQHS_loc_nokids_clinic.csv"), delimiter=",")
#FQHS_Ohio = {}
#for row in F_Ohio:
#    FQHS_Ohio[int(row['Unique_number'])] = row
 
# OTP locations 
#O_Ohio = csv.DictReader(open("/Users/si272/Documents/LiClipse Workspace/FQHS_OTP_LOC_OHIO/Location_coverage_model/OTP_loc.csv"), delimiter=",")
#OTP_Ohio = {}
#for row in O_Ohio:
#    OTP_Ohio[int(row['Unique_number'])] = row  

##################################################################################
# PASTE YOUR KEY HERE
BingMapsKey = "AhLCkmwHpj1Y0S5oKy7Bl4CRFRmEF0iRXH7LZV9Y6r9V4-GQUaAla_IdiywoUCSY"



key_value = loadtxt("/Users/si272/Documents/LiClipse Workspace/Bandit_NewHaven/Covid_Bandit_New_Locations_Lat_Long.csv", delimiter=",")
start_dict = { k :(float(v), float(w)) for k,v,w in key_value }


finish_dict = start_dict

inmiles = {}
count = 0
for key1 in start_dict:
    for key2 in finish_dict:
    
    #print ("key",key1, key2)
    
    #print ('finish', key2, finish_dict[key2][0],finish_dict[key2][1])
    #print ('start', key1,  start_dict[key1][0],start_dict[key1][1])
    
        start = '{},{}'.format(start_dict[key1][0],start_dict[key1][1])
        
        
       
        finish = '{},{}'.format(finish_dict[key2][0],finish_dict[key2][1])
        
        #print ("finish", key2, finish)
        #routeUrl = "http://dev.virtualearth.net/REST/V1/Routes?wp.0=" + start + "&wp.1="  + finish + "&key="+ BingMapsKey
        routeUrl = "http://dev.virtualearth.net/REST/v1/Routes/Driving?wayPoint.1=" + start + "&waypoint.2=" + finish + "&optimize=distance&routeAttributes=routeSummariesOnly&distanceUnit=mi&key="+ BingMapsKey
        r = requests.get(routeUrl)
        
        #print(r)
        #r = request.read().decode(encoding="utf-8")
        result = json.loads(r.content)
        
        #print (result)
        rtn = -1
        #try:
        print ('distance', key1, start_dict[key1][0],start_dict[key1][1], key2, finish_dict[key2][0],finish_dict[key2][1], result["resourceSets"][0]["resources"][0][u'travelDistance'])
        inmiles[key1,key2] = result["resourceSets"][0]["resources"][0][u'travelDistance']

f = open('real_distance_bandit_NewHaven_Locations.csv', 'w')
for key in inmiles.keys():
    f.write("%s,%s,%s\n" % (int(key[0]),int(key[1]),inmiles[key])) 
    
    
    
    
    
    