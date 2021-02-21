#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 13:10:08 2021
@author: pierre-etienne
"""
import discord, search, library, feed_back
import preprocessing as preproc
import datetime, time
import chatter_bot as ct
import pickle
from discord import ext


topics = ['data_sciences', 'artificial_intelligence', 'travel','music','movies','english']
keys = ['0','1','2','3','4','5']

client = discord.Client()

end = False
save = False
found = False

with open('/home/roger/anaconda3/projetIA/Chat_bot/ChatBot/topic_classifier.pkl','rb') as file:
    topic_clf = pickle.load(file)

@client.event
async def on_ready():
    print("Hello I am ", client.user)
    embed=discord.Embed(title="Jarvis", url="https://photos.google.com/search/_tra_", description="I am a bot", color=0x000000)
    await ctx.send(embed=embed)

@client.event
async def on_message(message):
    global topic, end, save, lan, found
    #traduction message user
    if message.content not in ['/help','/h'] and message.content not in keys:
        ms,lan = preproc.transin(message.content)
        msg = preproc.prep(ms)
    else:
        msg = message.content   
    
    if message.author != client.user:
        if msg in library.lib and end !=True :
            res = ct.chatter_bot_conv(msg)
            #reponse dans la langue user
            resp = preproc.transout(res,lan)
            await message.channel.send(resp)             
        else:   
            try:
                if msg not in library.lib and preproc.transout(msg,'fr') != 'non' and preproc.transout(msg,'fr') != 'oui' and end !=True: 
                    topic = topic_clf.predict([msg])[0]
                    print("search",topic_clf.predict([msg])[0])
                    resp = search.find_question_answer(msg,topic)
                    found = True
                    resp = preproc.transout(resp,lan)
                    await message.channel.send(resp[:2000])
            except NameError:
                if  preproc.transout(msg,'fr') != 'non' and end !=True:
                    response = preproc.transout('Pouvez-vous m\'en dire plus ?',lan)
                    await message.channel.send(response)                        
        # fin de conversation
        if found == True and msg not in library.lib and preproc.transout(msg,'fr') != 'non' and preproc.transout(msg,'fr') != 'oui'and msg not in keys and end !=True:
            resp = preproc.transout(library.end_of_conv[0], lan)
            await message.channel.send(resp)
        if preproc.transout(msg,'fr') == 'non':
            resp = preproc.transout(library.bot_end_conv[0],lan)
            await message.channel.send(resp)
            end = True
        if preproc.transout(msg,'fr') != 'non' and end == True and save == False:
            feed_back.add_feeback({"message":message.content,
                                    "date":str(datetime.date.today())}) 
            save = True                        
        

token = ''
client.run(token)