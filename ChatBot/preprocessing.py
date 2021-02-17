import string 

def prep(msg):
    #without ponctuation
    #msg = msg.sprit()
    if msg not in ['/help','/h']:
        msg = msg.translate(str.maketrans("","", string.punctuation)) 

    return msg.lower()