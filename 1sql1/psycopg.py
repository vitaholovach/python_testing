import psycopg2

try:
    connection = psycopg2.connect(
        user="postgres",
        password="Sofia2021@",
        host="127.0.0.1",
        dbname="sqlhillel"
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        pass

    # CREATE TABLE products
    with connection.cursor() as cursor:
        cursor.execute(
            "CREATE TABLE products (id SERIAL PRIMARY KEY, name VARCHAR(25),  price INTEGER)")
        connection.commit()
        print("Table created successfully")

    # CREATE TABLE orders
    with connection.cursor() as cursor:
        cursor.execute(
            "CREATE TABLE orders (id SERIAL PRIMARY KEY, product_id INTEGER,quantity INTEGER )")
        connection.commit()
        print("Table created successfully")

    # INSERT INTO orders
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO orders (id, product_id, quantity) VALUES (1,2,7), (2,3,3), (3,4,1), (4,2,5), (5,3,1)")
        connection.commit()
        print("Data was succefully inserted")

    # INSERT INTO products
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO products (id, name, price) VALUES (1,'cream',100), (2,'pomade', 20), (3, 'powder', 26), (4,'mascara', 260), (5,'eyeshadow', 455)")
        connection.commit()
        print("Data was succefully inserted")

    with connection.cursor() as cursor:
        cursor.execute("SELECT* from orders")
        print(cursor.fetchall())

    with connection.cursor() as cursor:
        cursor.execute("SELECT* from products")
        print(cursor.fetchall())

    with connection.cursor() as cursor:
        cursor.execute("SELECT p.name, p.price, o.quantity,  (p.price * o.quantity) AS total_price FROM products p "
                       "JOIN orders o ON p.id=o.product_id ORDER BY total_price DESC")
        print(cursor.fetchall())

finally:
    if connection:
        connection.close()
        print("PostgreSQL connection closed")
