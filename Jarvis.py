#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 13:10:08 2021
@author: pierre-etienne
"""

import discord, search
#import os

from nltk.chat.util import Chat, reflections
import chatter_bot
from bs4 import BeautifulSoup
import html2markdown

#welcome_message = open("/home/roger/anaconda3/projetIA/Chat_bot/ChatBot/welcome_message.html").read()
#welcomme_message = [BeautifulSoup(welcome_message, "lxml").text]

welcome_message = [html2markdown.convert("<p>How can I help you ? Here are all the topics we can talk about ! Just choose one with its key:<br>0 : Data_sciences<br>1 : Artificial Intelligence<br>2 : Travel<br>3 : Music<br>4 : Movies<br>5 : English</p>")]

topics = ['data_sciences', 'ai', 'travel','music','movies','english']
keys = ['0','1','2','3','4','5']

def print_topics():
    for k, v in enumerate(topics):
        print(k, v)
def append_topics(welcome_message):
    for v in topics:
        welcome_message.append(v) 

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"/help",
        welcome_message
    ],
    [
        r"/h",
        welcome_message
    ],
    [
        r"what about (.*)",
        welcome_message
    ],
     [
        r"what is your name ?",
        ["My name is Jarvis and I'm a chatbot ?",]
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
        ["No rain since last time.*)"]
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
        r"bye",
        ["Bye take care. See you soon :) ","It was nice talking to you. See you soon :)"]

],
    [
        r"quit",
        ["Bye take care. See you soon :) ","It was nice talking to you. See you soon :)"]

]
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
        if chat.respond(message.content):
            await message.channel.send(chat.respond(message.content))
            print(message.content)
        else :
            if message.content in keys: 
                topic = topics[int(message.content)]
                print(topic)
                print('Ok, what do you want to know about :', topic)
                await message.channel.send('Ok, what do you want to know about : %s'%topic)
            try:
                print(topic)
                #await message.channel.send('Can you tell me more ?') 
                #traitement de la question utilisateur pour recuperer l'objet de la question
                if message.content not in keys: 
                    resp = search.find_question_answer(message.content,topic)
                    await message.channel.send(resp[:2000])
            except NameError:
                resp = chatter_bot.chatter_bot_conv(message.content)
                await message.channel.send(resp)                

        
token = '...'
client.run(token)