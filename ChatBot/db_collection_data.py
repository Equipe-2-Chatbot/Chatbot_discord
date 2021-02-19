#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 00:13:18 2020

@author: caroline
"""

from pymongo import MongoClient
import xmltodict

client = MongoClient("localhost", 27017)
db = client["stackexchange"]

# define location of dataset
folder = 'name of the folder path containing the folders with the Posts.xml files'

import glob
# Using '*' pattern
list_coll=[]
for name in glob.glob(folder+'*'): 
    list_coll.append(name)
#print (list_coll)


for coll in list_coll:
  with open(coll+'/'+'Posts.xml') as fd:
      posts = xmltodict.parse(fd.read())

  posts_collection = db[coll[len(folder):-len('.stackexchange.com')]]
    
  for data in posts['posts']['row']:
    posts_collection.insert_one(data)
        
client.close()