from store_repository import StoreRepository


store_db = StoreRepository()
store_db.create_database("store")
store_db.use_database("store")
store_db.create_table("products", "id", "int auto_increment primary key",
                      "name", "varchar(255) not null", "price", "int not null")
store_db.create_table_with_condition("orders", "id", "int auto_increment primary key",
                      "product_id", "int", "quantity", "int not null",
                      "foreign key (product_id) references products(id)")
store_db.insert_into_table("products", "(name, price)", "('crema', 100),('pomade', 20),('powder', 26),('mascara', 260),('eyeshadow', 455)")
store_db.insert_into_table("orders", "(product_id, quantity)", "(1, 2),(2, 3),(3, 4),(4, 5),(5, 6)")
store_db.select_all_with_total_price()
