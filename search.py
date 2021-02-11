#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 00:13:18 2020

@author: roger
"""
from pymongo import MongoClient
import html2markdown

def find_question_answer(msg, topic):
    client = MongoClient("localhost", 27017)
    db = client["stackexchange"]
    question = db.get_collection(topic).find(
            { "$text": { "$search": msg } }).sort([("@Score",-1)]).limit(1)
    question = list(question) 
    if question !=[] : 
        questId  = question[0]['@Id']
        print('id question',questId)
        resp = db.get_collection(topic).find({"@ParentId":questId}).sort([('@Score', -1)]).limit(1)
        resp = list(resp)
        if resp !=[] : 
            resp = html2markdown.convert(resp[0]['@Body'])
        else:
            resp = 'Can you precise your question ?'    
    else :
        resp = 'Can you tell me more about it ?'           

    client.close()
    return resp