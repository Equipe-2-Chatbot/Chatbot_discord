from pymongo import MongoClient

def add_feeback(data):
    client = MongoClient("localhost", 27017)
    db = client["stackexchange"]
    feedback_collection = db["feedback"]        
    feedback_collection.insert_one(data)            
    client.close()