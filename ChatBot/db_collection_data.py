#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 00:13:18 2020

@author: roger
"""

from pymongo import MongoClient
import xmltodict

client = MongoClient("localhost", 27017)
db = client["stackexchange"]

with open('Posts.xml') as fd:
    posts = xmltodict.parse(fd.read())

posts_collection = db["english"]
    
for data in posts['posts']['row']:
    posts_collection.insert_one(data)
        
client.close()