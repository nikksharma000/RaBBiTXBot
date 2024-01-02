from config import MONGO_URI
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

mongo = MongoClient(MONGO_URI)

db = mongo.Bunny
