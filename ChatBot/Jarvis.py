#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 13:10:08 2021
@author: pierre-etienne, roger
"""
import discord, search, library, feed_back
import preprocessing as preproc
import datetime, time
import chatter_bot as ct
import pickle


topics = ['data_sciences', 'artificial_intelligence', 'quantum_computing','travel','music','movies']

client = discord.Client()

found = False
comment_flag = False

with open('/home/roger/anaconda3/projetIA/Chat_bot/ChatBot/topic_classifier.pkl','rb') as file:
    topic_clf = pickle.load(file)

@client.event
async def on_ready():
    print("Hello I am ", client.user)

@client.event
async def on_message(message):
    global topic, lan, found, comment_flag
    #traduction message user
    if message.content not in ['/help','/h']:
        ms,lan = preproc.transin(message.content)
        msg = preproc.prep(ms)
    else:
        msg = message.content   
    
    if message.author != client.user:
        #Gestion de la conversation
        if msg in library.lib and message.channel.name not in channel_closed and comment_flag == False:
            print(message.channel)
            if msg in ['hello'] or message.content in ['/help','/h']:       
                await message.channel.send(file=discord.File('/home/roger/anaconda3/projetIA/Chat_bot/ChatBot/robot.png'))
            res = ct.chatter_bot_conv(msg)
            #reponse dans la langue user
            resp = preproc.transout(res,lan) 
            await message.channel.send(resp)             
        else:
            #Gestion de la recherche en bdd   
            try:
                if msg not in library.lib and preproc.transout(msg,'en') != 'no' and comment_flag == False and preproc.transout(msg,'en') != 'yes' : 
                    topic = topic_clf.predict([msg])[0]
                    print("search",topic_clf.predict([msg])[0])
                    resp = search.find_question_answer(msg,topic)
                    found = True
                    resp = preproc.transout(resp,lan)
                    await message.channel.send(resp[:2000])
            except NameError:
                if  preproc.transout(msg,'en') != 'no' and comment_flag == False:
                    response = preproc.transout('Pouvez-vous m\'en dire plus ?',lan)
                    await message.channel.send(response)                        
        # fin de conversation
        if found == True and msg not in library.lib and preproc.transout(msg,'en') != 'no' and preproc.transout(msg,'en') != 'yes'and comment_flag == False:
            resp = preproc.transout(library.end_of_conv[0], lan)+library.end_of_conv[1]
            await message.channel.send(resp)
        if preproc.transout(msg,'en') == 'no' and comment_flag == False:
            resp = preproc.transout(library.bot_end_conv[0],lan)
            await message.channel.send(resp)
            comment_flag = True
            #channel_closed.append(message.channel.name)
        if preproc.transout(msg,'en') != 'no' and comment_flag == True :
            feed_back.add_feeback({"message":message.content,
                                    "date":str(datetime.date.today())})
            #channel_comment_saved.append(message.channel.name)
            comment_flag = False


token = ''
client.run(token)