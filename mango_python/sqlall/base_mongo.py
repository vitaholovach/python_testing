from pymango import MongoClient
from sqlall.config_reader import ReadConfig


class BaseMongo:
    def __init__(self, db_name, collection_name):
        self.client = MongoClient(ReadConfig.get_client_url())
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def show_databases(self):
        self.client.list_database_names()

    def insert_one(self, obj):
        self.collection.insert_one(obj)

    def insert_many(self, obj):
        self.collection.insert_many(obj)

    def find_one(self, key, value):
        print(self.collection.find_one({key: value}))

    def find_one_no_id(self, key, value):
        print(self.collection.find_one({key: value}, {"_id": 0}))

    def find_all(self):
        for element in self.collection.find({}, {"_id": 0}):
            print(element)

    def delete_one(self, key, value):
        self.collection.delete_one({key: value})

    def delete_all(self):
        self.collection.delete_many({})

    def delete_database(self):
        self.client.drop_database(self.db)
