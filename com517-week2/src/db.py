from pymongo import MongoClient
from config import MONGODB_URI, MONGODB_DB

client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=3000)
db = client[MONGODB_DB]
students = db["students"]

if __name__ == "__main__":
    client.admin.command("ping")
    print("Connected to", MONGODB_DB)