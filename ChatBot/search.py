#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 00:13:18 2020

@author: roger
"""
from pymongo import MongoClient
from bs4 import BeautifulSoup

def search(msg,db,topic):    
    question = db.get_collection(topic).find(
            { "$text": { "$search": msg } }).sort([("@Score",-1)]).limit(1)
    return question

def find_question_answer(msg, topic):
    print(msg)
    client = MongoClient("localhost", 27017)
    db = client["stackexchange"]
    #Faire une recherche par tags, tiltle et body dans cet ordre
    exp = "\"" + msg + "\""
    print(exp)
    question = search(exp,db,topic)
    question = list(question)
    print("exacte Q",question) 
    if question ==[] :
        question = search(msg,db,topic)
        question = list(question) 
        print("exacte mot cle",question) 
    if question !=[] : 
        questId  = question[0]['@Id']
        print('id question',questId)
        resp = db.get_collection(topic).find({"@ParentId":questId}).sort([('@Score', -1)]).limit(1)
        resp = list(resp)
        if resp !=[] : 
            print('resp ID',resp[0]['@Id'])
            resp = BeautifulSoup(resp[0]['@Body'], "lxml").text            
        else:
            resp = 'Can you precise your question ?'    
    else :
        resp = 'Can you tell me more about it ?'           

    client.close()
    return resp

