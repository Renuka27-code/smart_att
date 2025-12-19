# db.py
from pymongo import MongoClient

MONGO_URI = "mongodb+srv://Harshith:Harshith5197@cluster0.vu2q9ul.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client["algo_smart_attendance"]
collection = db["attendance"]