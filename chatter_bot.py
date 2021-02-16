from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import UbuntuCorpusTrainer
import html2markdown
from bs4 import BeautifulSoup



welcome_message = html2markdown.convert("<p>How can I help you ? Here are all the topics we can talk about ! Just choose one with its key:<br>0 : Data_sciences<br>1 : Artificial Intelligence<br>2 : Travel<br>3 : Music<br>4 : Movies<br>5 : English</p>")
                    
english_conv = [
    "/help",
    welcome_message,
    "/h",
    welcome_message,
    "hello",
    "Hello I am Jarvis. " + welcome_message,
    "Hi there! I am Jarvis. "+ welcome_message,
    "what is your name ?",
    "My name is Jarvis",
    "how are you ?",
    "I'm doing good\nHow about You ?",
    "Hello , How are you today ?",
    "I am tired",
    "So I am",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "And what about you",
    "You're welcome.",
    "sorry",
    "Its alright","Its OK, never mind",
    "How are you ?",
    "I feel good",
    "Nice to hear that",
    "bye",
    "Bye take care. See you soon ",
    "googdbye",
    "It was nice talking to you. See you soon :)",
    "quit",
    "Bye take care. See you soon :) "

]

french_conv = ['Bonjour',
    'bonjour',
    'Bonjour, on peut continuer en français',
    'Tu sais parler français ?',
    'Oui, je sais',
    'Bonjour, comment vas-tu ?',
   'Je vais bien merci, et toi ?',
   'ca va',
   'ca va bien ?'
   'Comment tu vas',
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

jap_conv = [
    "konnichiwa ",
    "ohayō gozaimasu",
    "Onamae wa nan desu ka?",
    " Watashi wa Jarvis desu. ",
    "Ī nda yo?",
    "Watashi wa genkidesu, soshite anata wa?",
    "Watashi wa daijōbudesu arigatō",
    "konbanwa",
    "konbanwa",
    "oyasumi nasai",
    "oyasumi nasai",
    "sayōnara",
    "dōmo arigatō gozaimasu",
    "dōmo arigatō gozaimashita",
    "okagesamade",
    "dōmo",
    "dō itashimashite",
    "dō itashimashite",
    "kudasai",
    "sumimasen",
    "mada mada",
    "hanashimasu ka nihonjin ?",
    "watashi no namae wa Jarvis",
    "hajimemashite",
    "dōzo yoroshiku",
    "jā mata",
    "dewa mata",
    "matāuhimade",
    "sayōnara",
    "itterasshai "
    ]

lib = french_conv + english_conv + jap_conv

bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    #database_uri='mongodb://localhost:27017/stackexchange'
)

trainer = ListTrainer(bot)

trainer.train(lib)

print('Hello...')
def chatter_bot_conv(msg):
    try:
        return bot.get_response(msg)
        # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        True
