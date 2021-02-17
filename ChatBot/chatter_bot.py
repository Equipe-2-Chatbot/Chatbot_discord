from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import UbuntuCorpusTrainer
import library


bot = ChatBot(
    'Jarvis',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        #'chatterbot.logic.MathematicalEvaluation',
        #'chatterbot.logic.TimeLogicAdapter',
    ],
    database_uri='mongodb://localhost:27017/chatter_bot'
)
bot.storage.drop()

trainer = ListTrainer(bot)
lib = [library.french_conv, library.english_conv, library.jap_conv, library.greetings, library.conversations]
for l in lib:
    trainer.train(l)
trainer.train(library.english_conv)
print('Hello...')
def chatter_bot_conv(msg):
    try:  
        return bot.get_response(msg)
        # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        True
