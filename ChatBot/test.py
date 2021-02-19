import html2markdown
import yaml

with open("/home/roger/anaconda3/projetIA/Chat_bot/ChatBot/french_conversations.yml", 'r') as stream:
    out = yaml.load(stream)
    dico = out['conversations']
french_conversation = []
for elt in dico:
    french_conversation+=elt
print(french_conversation)

msg = "Ca va"
if msg in french_conversation:
    print('OK')

import re, string
test = "CA, VA ?!!!"
test = test.translate(str.maketrans("","", string.punctuation)) 
test = test.lower()
print(test)
# fline = re.sub('['+string.punctuation+']', '', "CA, VA ?!!!")
# print(fline)
# clean_string = re.sub(rf"[{string.punctuation}]", "", "CA, VA ?!!!")
# print(clean_string)

