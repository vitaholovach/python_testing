from collection_products import CollectionProducts
from collection_brands import CollectionBrands
from sqlall.config_reader import ReadConfig

coll_brands, coll_products = CollectionBrands(), CollectionProducts()

if __name__ == "__main__":
    coll_brands.insert_many(ReadConfig.get_brands_collection_document())
    coll_brands.find_all()

    coll_products.insert_many(ReadConfig.get_products_collection_document())
    coll_products.find_all()

    coll_products.find_one("brand", "Rabbithole")
    coll_brands.find_one_no_id("brand", "Clarins")

    coll_brands.delete_one("brand", "Clarins")
    coll_brands.find_all()

    coll_brands.delete_all()
    coll_brands.find_all()
    coll_products.find_all()
