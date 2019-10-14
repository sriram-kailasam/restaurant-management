import sqlite3
import os

conn = sqlite3.connect(os.path.join(os.getcwd(), "restaurant.db"))

def create_restaurants_table(conn):
    cur = conn.cursor()

    q = """
        CREATE TABLE IF NOT EXISTS restaurants (
            id integer PRIMARY KEY,
            name text,
            address text
        );
    """

    cur.execute(q)
    conn.commit()

def create_orders_table(conn):
    cur = conn.cursor()

    q = """
        CREATE TABLE IF NOT EXISTS orders (
            id integer PRIMARY KEY,
            item_id integer,
            customer_id integer,
            restaurant_id integer,
            datetime text,

            FOREIGN KEY(item_id) REFERENCES items(id),
            FOREIGN KEY(customer_id) REFERENCES customers(id),
            FOREIGN KEY(restaurant_id) REFERENCES restaurants(id)
        );
    """

    cur.execute(q)
    conn.commit()

def create_customers_table(conn):
    cur = conn.cursor()

    q = """
        CREATE TABLE IF NOT EXISTS customers (
            id integer PRIMARY KEY,
            name text,
            age integer,
            gender text
        );
    """

    cur.execute(q)
    conn.commit()

def create_items_table(conn):
    cur = conn.cursor()

    q = """
        CREATE TABLE IF NOT EXISTS items (
            id integer PRIMARY KEY,
            restaurant_id integer,
            name text,
            price numeric,

            FOREIGN KEY(restaurant_id) REFERENCES restaurants(id)
        );
    """

    cur.execute(q)
    conn.commit()

def create_reviews_table(conn):
    cur = conn.cursor()

    q = """
        CREATE TABLE IF NOT EXISTS reviews  (
            id integer PRIMARY KEY,
            restaurant_id integer,
            customer_id integer,
            review text,
            rating numeric CHECK(rating >= 1 AND rating <= 5),

            FOREIGN KEY(restaurant_id) REFERENCES restaurants(id),
            FOREIGN KEY(customer_id) REFERENCES customers(id)
        );
    """
    cur.execute(q)
    conn.commit()
    

def populate_restaurants_table(conn):
    cur = conn.cursor()

    q = """
        INSERT INTO restaurants VALUES (?, ?, ?)
    """
    restaurants = [
        (1, "Green Palace", "Main Street, Gandhidham"),
        (2, "Purohit Garden Restaurant", "Side Street, Gandhidham"),
        (3, "Neo Politon Pizza", "Gandhi Circle, Ahmedabad"),
        (4, "Satyam Foods", "Rotary Circle, Anjar"),
        (5, "Agra Food Center",  "Main Highway, Agra")
    ]

    cur.executemany(q, restaurants)
    conn.commit()

def populate_customers_table(conn):
    cur = conn.cursor()

    q = """
        INSERT INTO customers VALUES (?, ?, ?, ?)
    """
    customers = [
        (1, "John Doe", 25, "Male"),
        (2, "Jane Doe", 22, "Female"),
        (3, "David Smith", 33, "Male"),
        (4, "Elizabeth", 45, "Female"),
        (5, "Rakesh Singh", 19, "Male")
    ]

    cur.executemany(q, customers)
    conn.commit()

def populate_reviews_table(conn):
    cur = conn.cursor()

    q = """
        INSERT INTO reviews VALUES (?, ?, ?, ?, ?)
    """

    reviews = [
        (1, 1, 1, "Amazing food at a low price.", 5),
        (2, 1, 2, "Decent food.", 4),
        (3, 2, 3, "Good food but took a lot of time.", 3.5),
        (4, 3, 1, "Very costly.", 3.5),
        (5, 3, 2, "Okayish food.", 3.5),
        (6, 4, 4, "Snacks were great.", 4),
        (7, 5, 5, "Incredible!", 5)
    ]

    cur.executemany(q, reviews)
    conn.commit()

def populate_items_table(conn):
    cur = conn.cursor()

    q = """
        INSERT INTO items VALUES (?, ?, ?, ?)
    """
    items = [
        (1, 1, "Veg Maharaja", 200),
        (2, 2, "Veg Pulao", 150),
        (3, 3, "Unlimited Meal", 300),
        (4, 4, "Pav Bhaji", 100),
        (5, 5, "Veg Burger", 50),
        (6, 1, "Butter Naan", 40),
        (7, 2, "Masala Dosa", 100),
        (8, 3, "Margherita", 150)
    ]

    cur.executemany(q, items)
    conn.commit()

def populate_orders_table(conn):
    cur = conn.cursor()

    q = """
        INSERT INTO items VALUES (?, ?, ?, ?, ?)
    """

    orders = [
        (1, 1, 1, 1, "2019-08-30 18:47"),
        (2, 2, 2, 2, "2019-08-29 18:47"),
        (3, 3, 3, 3, "2019-09-30 16:47"),
        (4, 4, 4, 4, "2019-08-30 18:27"),
        (5, 5, 5, 5, "2019-06-30 08:47"),
        (6, 6, 2, 1, "2019-08-21 16:45"),
        (7, 7, 4, 2, "2019-08-30 18:47"),
        (8, 8, 1, 3, "2019-10-30 09:36")
    ]

    cur.executemany(q, orders)
    conn.commit()

create_items_table(conn)
create_customers_table(conn)
create_orders_table(conn)
create_restaurants_table(conn)
create_reviews_table(conn)

populate_customers_table(conn)
populate_restaurants_table(conn)
populate_reviews_table(conn)
populate_items_table(conn)
populate_orders_table(conn)