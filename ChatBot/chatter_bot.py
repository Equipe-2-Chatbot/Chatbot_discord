from chatterbot import ChatBot
from chatterbot import corpus
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import UbuntuCorpusTrainer
import library
import string 

bot = ChatBot(
    'Jarvis',read_only = True,
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.unescape_html',
        'chatterbot.preprocessors.convert_to_ascii'
    ],
    logic_adapters=[{
        #'chatterbot.logic.BestMatch',
        'import_path': 'chatterbot.logic.BestMatch',
        "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
        #'chatterbot.logic.MathematicalEvaluation',
        #'chatterbot.logic.TimeLogicAdapter',
        'default_response': 'I am sorry, but I do not understand.',
        'maximum_similarity_threshold': 0.90}
     ],    
    database_uri='mongodb://localhost:27017/chatter_bot'
)

def clean_ponctuation(statement):
    """
    Remove any ponctuation characters from the statement text.
    """
    import re
    # Replace -  with spaces
    statement.text = statement.text.replace('-', ' ')
    statement.text = statement.text.translate(str.maketrans("","", string.punctuation)) 
    statement.text = statement.text.lower()
    return statement

# bot.preprocessors.append(
#     clean_ponctuation
# )

#bot.storage.drop()

trainer = ListTrainer(bot)
lib = [library.english_conv, library.greetings, library.conversations]
for l in lib:
    trainer.train(l)

# trainer = ChatterBotCorpusTrainer(bot)
# trainer.train('chatterbot.corpus.english.conversations')
print('Hello...')
def chatter_bot_conv(msg):
    try:  
        return bot.get_response(msg)
        # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        True
