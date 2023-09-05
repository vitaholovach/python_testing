from base_repository import BaseRepository


class StoreRepository(BaseRepository):
    def __init__(self):
        super().__init__()

    def create_table(self, table_name, column_1, type_1, column_2, type_2, column_3, type_3):
        self.cursor.execute(f"create table {table_name} ({column_1} {type_1},{column_2} {type_2},{column_3} {type_3});")

    def create_table_with_condition(self, table_name, column_1, type_1, column_2, type_2, column_3, type_3, condition):
        self.cursor.execute(
            f"create table {table_name} ({column_1} {type_1},{column_2} {type_2},{column_3} {type_3},{condition});")

    def select_all_with_total_price(self):
        self.cursor.execute(
            "select p.name, p.price, o.quantity, (p.price * o.quantity) as total_price from products p join orders o ON p.id = o.product_id;")
        for product in self.cursor.fetchall():
            print(product)
