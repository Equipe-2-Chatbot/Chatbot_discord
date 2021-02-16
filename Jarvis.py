#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 13:10:08 2021
@author: pierre-etienne
"""

import discord, search
#import os

#from nltk.chat.util import Chat, reflections
import chatter_bot as ct
import chatter_bot_school as ct_school

topics = ['data_sciences', 'ai', 'travel','music','movies','english']
keys = ['0','1','2','3','4','5']


client = discord.Client()

@client.event
async def on_ready():
    print("Hello I am ", client.user)

@client.event
async def on_message(message):
    global topic
    if message.author != client.user:        
        if message.content in ct.lib:
            resp = ct.chatter_bot_conv(message.content)
            await message.channel.send(resp) 
        else:
            if message.content in ct_school.lib :
                resp = ct_school.chatter_bot_conv(message.content)
                await message.channel.send(resp) 

            if message.content in keys: 
                topic = topics[int(message.content)]
                print(topic)
                print('Ok, what do you want to know about :', topic)
                await message.channel.send('Ok, what do you want to know about : %s'%topic)
            try:
                print(topic)
                if message.content not in (keys + ct.lib): 
                    resp = search.find_question_answer(message.content,topic)
                    await message.channel.send(resp[:2000])
            except NameError: 
                await message.channel.send('Can you tell me more ?')                        

        
token = 'ODA4NjI4MDAxMjQ3MzMwMzA1.YCJTgw.kyL8xZKyBs1Yw82KEPPIIpZFZG8'
# token = 'ODA4NjQ1ODkzOTk2ODA2MTU0.YCJkLQ.4mLKI_wpqCKsln25zD3BKSeOWgY'
client.run(token)