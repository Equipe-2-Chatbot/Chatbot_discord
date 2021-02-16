from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import UbuntuCorpusTrainer
import html2markdown
from bs4 import BeautifulSoup

bot_school = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    #database_uri='mongodb://localhost:27017/stackexchange'
)

msg_bienvenue = html2markdown.convert("<p>Qu'est-ce que je peux faire pour toi ? Voici tous les sujets qu'on peut voir ensemble : TApes juste 0 pour la musique:<br>0 : musique</p>")
                    
french_conv = ['Tu t\'appeles comment ?',
    'Je m\'appelle Jarvis',
    'Tu t\'appeles comment ?',
    'Je m\'appelle Jarvis'
    ]

lib = french_conv

trainer = ListTrainer(bot_school)

trainer.train(lib)

print('Hello...')
def chatter_bot_conv(msg):
    try:
        return bot_school.get_response(msg)
        # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        True
