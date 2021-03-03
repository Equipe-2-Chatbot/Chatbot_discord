# Chatbot_discord done with Chatterbot, some machine learning and Python

# To install the dependencies:
  pip install -r requirements.txt
  
# Data:
  Comes from Stachexchange (in xml format). 
  Use the db_collection_data.py to add the data to your Mongodb collections

# Change the settings:
  The token for your bot in Discord and the links to your project

# Launch the application :
  Jarvis.py
  
# Machine learning:
  A pickle data has been made by a SGD classifier and CountVectorizer on the questions from Stackexchange to learn from the different topics
  The Chatterbot learns from the library all the conversation it needs
  
# Preprocessing:
  It allows to translate in more than 100 languages from the Google app as it is included in a Python module, the user questions and the bot response

# Feedback:
  There is a feedback process to get the user feedbacks and add them in the mongodb database

  
 

