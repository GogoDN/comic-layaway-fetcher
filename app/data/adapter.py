from pymongo import MongoClient

from ..config import settings


class MongoDbClient:
    def __init__(self) -> None:
        self.client = MongoClient(settings.mongo_db_conn_str)

    def __get_comic_store_db(self):
        return self.client.comic_store

    def __get_layaways_collection(self):
        db = self.__get_comic_store_db()
        return db.layaways

    def find_one_by_user_id(self, user_id):
        collection = self.__get_layaways_collection()
        return collection.find_one({"user_id": user_id})
