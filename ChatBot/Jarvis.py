#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 13:10:08 2021
@author: pierre-etienne
"""

import discord, search, library, preprocessing
#import os

from nltk.chat.util import Chat, reflections
import chatter_bot as ct


topics = ['data_sciences', 'ai', 'travel','music','movies','english']
keys = ['0','1','2','3','4','5']

client = discord.Client()

@client.event
async def on_ready():
    print("Hello I am ", client.user)

@client.event
async def on_message(message):
    global topic
    msg = preprocessing.prep(message.content)
    if message.author != client.user:            
        if msg in library.lib :
            resp = ct.chatter_bot_conv(msg)
            await message.channel.send(resp)             
        else:    
            if msg in keys: 
                topic = topics[int(msg)]
                print(topic)
                print('Ok, what do you want to know about :', topic)
                await message.channel.send('Ok, what do you want to know about : %s'%topic)
            try:
                print(topic)
                if msg not in (keys + library.lib): 
                    resp = search.find_question_answer(msg,topic)
                    await message.channel.send(resp[:2000])
            except NameError:
                if  msg != 'non':
                    await message.channel.send('Can you tell me more ?')                        
        # fin de conversation
        if  msg != 'non':            
            await message.channel.send(library.end_of_conv[0])
        print(msg)
        if  msg == 'non':
            await message.channel.send(library.bot_end_conv[0])
        #await message.channel.send(msg)       
        
token = 'ODA4NjI4MDAxMjQ3MzMwMzA1.YCJTgw.RV-OiRYAtKL4ia0WuIWHYqh4ZQc'
#token = 'ODA4NjQ1ODkzOTk2ODA2MTU0.YCJkLQ._F8gfl_Rxs_oh9foJ06h1PjbCcs'
client.run(token)