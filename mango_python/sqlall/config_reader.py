import configparser
import json

config = configparser.RawConfigParser()
config.read("./configurations/config")


class ReadConfig:
    @staticmethod
    def get_client_url():
        return config.get("client_data", "client_url")

    @staticmethod
    def get_brands_collection_document():
        my_brands = config.get("collections_data", "my_brands")
        return json.loads(my_brands)

    @staticmethod
    def get_products_collection_document():
        my_products = config.get("collections_data", "my_products")
        return json.loads(my_products)
