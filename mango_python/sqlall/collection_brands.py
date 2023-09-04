from base_mongo import BaseMongo


class CollectionBrands(BaseMongo):
    def __init__(self):
        super().__init__('companies', 'brands')
