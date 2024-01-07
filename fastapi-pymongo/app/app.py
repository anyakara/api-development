from fastapi import FastAPI
from routes.todo_routes import router

app = FastAPI()
app.include_router(router)

from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://<username>:<password>@cluster0.cump9sk.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri) #, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
