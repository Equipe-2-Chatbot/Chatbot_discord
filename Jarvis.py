#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 13:10:08 2021

@author: pierre-etienne
"""

import discord, search
#import os

from nltk.chat.util import Chat, reflections

welcome_message = ["Here are all the topics we can talk about ! Just choose one with its key:  0 : data_sciences, 1 : travel , 2 : music"]
topics = ['data_sciences', 'travel','music']

def print_topics():
    for k, v in enumerate(topics):
        print(k, v)
def append_topics(welcome_message):
    for v in topics:
        welcome_message.append(v)  

#append_topics(welcome_message)

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"/help",
        ["How can I help you ?",]
    ],
    [
        r"what can you tell me about (.*)",
        welcome_message
    ],
     [
        r"what is your name ?",
        ["My name is Chatty and I'm a chatbot ?",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?",]

    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]

    ],
    [
        r"(.*) created ?",
        ["Nagesh created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Chennai, Tamil Nadu',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
[
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony"]
],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
],
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]

],
]

client = discord.Client()

@client.event
async def on_ready():
    print("Hello I am ", client.user)
    print("Here are all the topics we can talk about ! Just choose one with its key")
    print(print_topics())

chat = Chat(pairs, reflections)

@client.event
async def on_message(message):
    global topic
    if message.author != client.user:
        #await message.channel.send(message.content[::-1])
        if chat.respond(message.content):
            await message.channel.send(chat.respond(message.content))
            print(message.content)
        else :
            if message.content in ['0','1','2']: 
                topic = topics[int(message.content)]
                print('Ok, what do you want to know about :', topic)
                await message.channel.send('Ok, what do you want to know about : %s'%topic)
            if topic != "":
                print(topic)
                await message.channel.send('Can you tell me more ?')  
                resp = search.find_question_answer(message.content,topic)
                await message.channel.send(resp[:2000])        

#token = os.environ.get("DISCORD_BOT_SECRET")
token = 'ODA4NjI4MDAxMjQ3MzMwMzA1.YCJTgw.MQY4WdHStAqO2gCbEzd48lKBKlM'
client.run(token)
