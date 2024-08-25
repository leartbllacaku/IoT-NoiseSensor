from pymongo import MongoClient

def get_db():
    client = MongoClient("mongodb+srv://<username>:<password>@cluster0.mongodb.net/mydatabase?retryWrites=true&w=majority")
    return client.mydatabase