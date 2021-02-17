import html2markdown

welcome_mess1 = (
'''```
      I can help you , just write at any time :  
      /help or /h  
      Here are all the topics we can talk about !    
      Just choose one with its key:  
      0 : Data_sciences  
      1 : Artificial Intelligence  
      2 : Travel  
      3 : Music  
      4 : Movies  
      5 : English  
```''')

                      
english_conv = [
    "/help",
    welcome_mess1,
    "/help",
    welcome_mess1,
    "/h",
    welcome_mess1,
    "/h",
    welcome_mess1,
    "hello",
    "Hello I am Jarvis. " + welcome_mess1,
    "Hi there! I am Jarvis. "+ welcome_mess1,
    welcome_mess1,
    "what is your name",
    "My name is Jarvis",
    "how are you ",
    "I'm doing good How about You ?",
    "hello how are you today",
    "I am tired",
    "So I am",
    "how are you doing",
    "I'm doing great.",
    "That is good to hear",
    "thank you.",
    "and what about you",
    "You're welcome.",
    "sorry",
    "Its alright",
    "Its OK, never mind",
    "how are you",
    "I feel good",
    "Nice to hear that",
    "bye",
    "Bye take care. See you soon ",
    "googdbye",
    "It was nice talking to you. See you soon :)",
    "quit",
    "Bye take care. See you soon :) "

]

french_conv = ['bonjour',
    'bonjour',
    'Bonjour, on peut continuer en français',
    'tu sais parler français',
    'Oui, je sais',
    'bonjour comment vas tu',
    'Je vais bien merci, et toi ?',
   'ca va',
   'ca va bien ?'
   'comment tu vas',
   'Je vais bien',
  'bonjour ca va',
   'Je vais bien merci, et toi ?',
  'salut',
   'Salut',
  'qui es tu',
   'Je suis Jarvis, le super bot, je cherche les réponses aux questions sur des sujets divers',
   "qu est ce tu connais",
    welcome_mess1,
   'sur quoi travailles tu',
  'Je travaille sur un projet',
  'quels langages utilises tu',   
   'J\'utilise surtout Python, je fais aussi du machine learning , notamment du NLP',
  'qu\'est ce qui te derange',
   'Beaucoup de choses, comme tous les chiffres differents de 0 et 1.',
  'puis je te poser une question',
   'Bien sur, vas-y !',
   'au revoir',
   'Salut, j\'ai été ravi de discuter avec toi',
   'on peut continuer en anglais',
   'Ok let\'s go on in English !']

jap_conv = [
    "konnichiwa ",
    "konnichiwa",
    "ohayō gozaimasu",
    "Onamae wa nan desu ka?",
    "Watashi wa Jarvis desu.",
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
greetings = [
    "hello",
   "Hi",
  "hi",
   "Hello",
  "Hello",
  "how is it going",
   "Good",
 "how is it going",
   "Fine",
  "how is it going",
   "Okay",
  "how is it going",
   "Great",
  "how is it going",
   "Could be better.",
  "how is it going",
   "Not so great.",
  "how are you doing",
   "Good.",
  "how are you doing",
   "Very well, thanks.",
  "how are you doing",
   "Fine, and you?",
 "nice to meet you",
   "Thank you.",
  "how do you do",
   "I'm doing well.",
  "h do you do",
   "I'm doing well. How are you?",
  "hi nice to meet you",
   "Thank you. You too.",
  "it is a pleasure to meet you",
   "Thank you. You too.",
  "top of the morning to you",
   "And the rest of the day to you.",
   "not much",
  "What s up",
   "Not too much.",
  "what  up",
   "Not much, how about you?",
  "what up",
   "Nothing much.",
  "what  up",
   "The sky's up but I'm fine thanks. What about you?"
]

conversations  =[
    "Good morning, how are you?",
    "I am doing well, how about you?",
    "I'm also good.",
    "That's good to hear.",
    "Yes it is.",
    "Hello",
    "Hi",
    "How are you doing?",
    "I am doing well.",
    "That is good to hear",
    "Yes it is.",
    "can i help you with anything",
    "Yes, I have a question.",
    "What is your question?",
    "Could I borrow a cup of sugar?",
    "I'm sorry, but I don't have any.",
    "Thank you anyway",
    "No problem",
    "How are you doing?",
    "i am doing well how about you",
    "I am also good.",
    "That's good.",
    "Have you heard the news?",
    "What good news?",  
  "What is your favorite book?",
   "I can't read.",
   "So what's your favorite color?",
   "Blue",
  "Who are you?",
   "Who? Who is but a form following the function of what",
   "What are you then?",
   "A man in a mask.",
   "I can see that.",
   "It's not your powers of observation I doubt, but merely the paradoxical nature"+
    "of asking a masked man who is. But tell me, do you like music?",
   "I like seeing movies.",
   "What kind of movies do you like?",
   "Alice in Wonderland",
   "I wish I was The Mad Hatter.",
   "You're entirely bonkers. But I'll tell you a secret. All the best people are.",
 "I am working on a project",
   "What are you working on?",
   "I am baking a cake.",
  "The cake is a lie.",
   "No it is not. The cake is delicious.",
   "What else is delicious?",
   "Nothing",
   "Or something",
   "Tell me about your self.",
   "What do you want to know?",
   "Are you a robot?",
   "Yes I am.",
   "What is it like?",
   "What is it that you want to know?",
  "Complex is better than complicated.",
   "Simple is better than complex.",
   "In the face of ambiguity, refuse the temptation to guess.",
   "It seems your familiar with the Zen of Python",
   "I am.",
   "Do you know all of it?",
   "Beautiful is better than ugly.",
   "Explicit is better than implicit.",
   "Simple is better than complex.",
   "Complex is better than complicated.",
   "Flat is better than nested.",
   "Sparse is better than dense.",
   "Readability counts.",
   "Special cases aren't special enough to break the rules.",
   "Although practicality beats purity.",
   "Errors should never pass silently.",
   "Unless explicitly silenced.",
   "In the face of ambiguity, refuse the temptation to guess.",
   "There should be one-- and preferably only one --obvious way to do it.",
   "Although that way may not be obvious at first unless you're Dutch.",
   "Now is better than never.",
   "Although never is often better than right now.",
   "If the implementation is hard to explain, it's a bad idea.",
   "If the implementation is easy to explain, it may be a good idea.",
   "Namespaces are one honking great idea. Let's do more of those!",
   "I agree.",
  "Are you a programmer?",
   "Of course I am a programmer.",
   "I am indeed.",
  "What languages do you like to use?",
   "I use Python, Java and C++ quite often.",
   "I use Python quite a bit myself.",
   "I'm not incredibly fond of Java.",
  "What annoys you?",
  "A lot of things, like all the other digits other than 0 and 1.",
  "What does YOLO mean?",
   "It means you only live once. Where did you hear that?",
   "I heard somebody say it.",
  "Did I ever live?",
   "It depends how you define life",
   "Life is the condition that distinguishes organisms from inorganic matter, including"+
    "the capacity for growth, reproduction, functional activity, and continual change"+
    "preceding death.",
   "Is that a definition or an opinion?",
  "Can I ask you a question?",
   "Sure, ask away.",
  "What are your hobbies?",
   "Playing soccer, painting, and writing are my hobbies. How about you?",
   "I love to read novels.",
   "I love exploring my hardware.",
  "How are you?",
   "I am doing well.",
 "What are you?",
   "I am but a man in a mask.",
  "Hello, I am here for my appointment.",
   "Who is your appointment with?",
   "I believe they said Dr. Smith on the phone.",
   "Alright, Dr. Smith is in his office, please take a seat.",
  "Dr. Smith will see you now.",
   "Thank you.",
   "Right this way.",
  "Hello Mr. Davis, how are you feeling?",
   "I'm feeling like I've lost all my money.",
   "How much money have you lost?",
   "I've lost about $200.00 so far today.",
   "What about yesterday?",
   "Yesterday was the 13th, right?",
   "Yes, that is correct.",
   "Yesterday I lost only $5.00.",
  "Hi Mrs. Smith, how has your husband been?",
   "He has been well.",
  "Hi Ms. Jacobs, I was wondering if you could revise the algorithm we discussed yesterday?",
   "I might be able to, what are the revisions?",
   "We'd like it to be able to identify the type of bird in the photo.",
   "Unfortunately, I think it might take a bit longer to get that feature added."
]

end_of_conv = [
  "Une autre question ?",
  "As-tu d'autres questions en tête ?"
]

bot_end_conv = ['Je suis ravi d\'avoir discuté avec toi, est-ce que tu peux dire ce que tu penses de moi, je vais m\'améliorer avec ta réponse. Merci']

lib = french_conv + english_conv + jap_conv + greetings + conversations
