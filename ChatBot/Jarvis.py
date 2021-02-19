#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 13:10:08 2021
@author: pierre-etienne
"""
import discord, search, library, preprocessing, feed_back
#import os
import datetime, time
from nltk.chat.util import Chat, reflections
import chatter_bot as ct

topics = ['data_sciences', 'ai', 'travel','music','movies','english']
keys = ['0','1','2','3','4','5']

client = discord.Client()

end = False
save = False

@client.event
async def on_ready():
    print("Hello I am ", client.user)

@client.event
async def on_message(message):
    global topic, end, save
    msg = preprocessing.prep(message.content)
    if message.author != client.user:
        if msg in library.lib and end !=True:
            resp = ct.chatter_bot_conv(msg)
            print("rep de chatterbot traduit en fr",resp)
            await message.channel.send(resp)             
        else:    
            if msg in keys and end !=True: 
                topic = topics[int(msg)]
                print(topic)
                print('Ok, what do you want to know about :', topic)
                await message.channel.send('Ok, what do you want to know about : %s'%topic)
            try:
                print(topic)
                if msg not in (keys + library.lib) and msg != 'non' and end !=True: 
                    resp = search.find_question_answer(msg,topic)
                    await message.channel.send(resp[:2000])
            except NameError:
                if  msg != 'non' and end !=True:
                    await message.channel.send('Can you tell me more ?')                        
        # fin de conversation
        print(msg)
        if search.find_question_answer(msg,topic) and msg not in library.lib and msg != 'non' and msg != 'oui'and msg not in keys and end !=True:
            await message.channel.send(library.end_of_conv[0])
        if msg == 'non':
            await message.channel.send(library.bot_end_conv[0])
            end = True
        if msg != 'non' and end == True and save == False:
            feed_back.add_feeback({"message":message.content,
                                    "date":str(datetime.date.today())}) 
            save = True                        
  
token = ''
client.run(token)