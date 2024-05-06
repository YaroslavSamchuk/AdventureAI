from pymongo import MongoClient
import pymongo

client = MongoClient("mongodb+srv://samchukyaroslavofficial:228000@mydatabase.iynnyp9.mongodb.net/")
print(client.list_database_names())
database = client['AdventureAI']
print(database.list_collection_names())
history = database['history']

# print(database.list_database_names())
# print(pymongo.__version__)

# adventureai = database['AdventureAI']
# history = adventureai['history']
messages = history.find_one({'ip': "121221212121212"})
print(messages['messages'])