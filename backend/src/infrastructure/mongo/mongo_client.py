from pymongo import MongoClient

from src.infrastructure.settings import settings


def get_mongo_client() -> MongoClient:
    return MongoClient(
        host=settings.mongo.host,
        port=settings.mongo.port
    )
