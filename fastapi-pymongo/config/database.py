from pymongo import MongoClient
uri = "mongodb+srv://annykarra:monkey1234@cluster0.cump9sk.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

database = client.todo_db
collection_name = database['todo_collection']