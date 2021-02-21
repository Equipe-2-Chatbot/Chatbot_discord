import string 
from google_trans_new import google_translator

def prep(msg):
    #without ponctuation
    if msg not in ['/help','/h']:
        msg = msg.translate(str.maketrans("","", string.punctuation)) 
        msg = msg.lower()
    return msg

def transin(x):
    translator = google_translator()
    lan = translator.detect(x)[0]
    #print("transin",lan)
    out = translator.translate(x)
    out = out.strip()
    #print('out',out)
    return out,lan

def transout(x,lan):
    translator = google_translator()
    #print("transout",lan)
    out = translator.translate(x, lang_tgt=lan)
    out = out.strip()
    return out