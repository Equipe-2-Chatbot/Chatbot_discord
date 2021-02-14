from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import UbuntuCorpusTrainer

bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    database_uri='mongodb://localhost:27017/stackexchange'
)
conversation = [
    "Hello",
    "Hi there!",
    "I am tired",
    "So I am",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "And what about you"
    "You're welcome."
]

french_conv = ['Bonjour',
    'Bonjour, on peut continuer en français',
    'Tu sais parler français ?',
    'Oui, je sais',
    'Bonjour, comment vas-tu ?',
   'Je vais bien merci, et toi ?',
   'Ca va',
   'Je vais bien',
  'Bonjour, ca va ?',
   'Je vais bien merci, et toi ?',
  'Salut',
   'Salut',
  'Qui es-tu ?',
   'Je suis Jarvis, le super bot, je cherche les réponses aux questions sur des sujets divers',
   'Sur quoi travailles-tu ?',
  'Je travaille sur un projet',
  'Quels langages utilises-tu ?',   
   'J\'utilise surtout Python, je fais aussi du machine learning , notamment du NLP',
  'Qu\'est ce qui te derange ?',
   'Beaucoup de choses, comme tous les chiffres differents de 0 et 1.',
  'Puis-je te poser une question ?',
   'Bien sur, vas-y !',
   'Au revoir',
   'Salut, j\'ai été ravi de discuter avec toi',
   'On peut continuer en anglais pour les sujets techniques ?',
   'Ok let\'s go on in English !']

trainer = ListTrainer(bot)

trainer.train(french_conv)

print('Hello...')
def chatter_bot_conv(msg):
    try:
        return bot.get_response(msg)
        # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        True

#while True:
    #try:
        #user_input = input()
        #bot_response = bot.get_response(user_input)
        #print(bot_response)
        # Press ctrl-c or ctrl-d on the keyboard to exit
    #except (KeyboardInterrupt, EOFError, SystemExit):
        #break