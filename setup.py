import sqlite3
import os

conn = sqlite3.connect(os.path.join(os.getcwd(), "restaurant.db"))

def create_restaurants_table(conn):
    cur = conn.cursor()

    q = """
        CREATE TABLE restaurants (
            id integer PRIMARY KEY,
            name text,
            address text
        );
    """

    cur.execute(q)

def create_orders_table(conn):
    cur = conn.cursor()

    q = """
        CREATE TABLE orders (
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

def create_customers_table(conn):
    cur = conn.cursor()

    q = """
        CREATE TABLE customers (
            id integer PRIMARY KEY
        );
    """

    cur.execute(q)

def create_items_table(conn):
    cur = conn.cursor()

    q = """
        CREATE TABLE items (
            id integer PRIMARY KEY,
            restaurant_id integer,
            customer_id integer,
            rating numeric CHECK(rating >= 1 AND rating <= 5),

            FOREIGN KEY(restaurant_id) REFERENCES restaurants(id),
            FOREIGN KEY(customer_id) REFERENCES customers(id)
        );
    """


    cur.execute(q)

def create_reviews_table(conn):
    cur = conn.cursor()

    q = """
        CREATE TABLE items (
            id integer PRIMARY KEY,
            restaurant_id integer,
            customer_id integer,
            review text,
            rating numeric,

            FOREIGN KEY(restaurant_id) REFERENCES restaurants(id),
            FOREIGN KEY(customer_id) REFERENCES customers(id)
        );
    """
    cur.execute(q)

create_items_table(conn)
create_customers_table(conn)
create_orders_table(conn)
create_restaurants_table(conn)
create_reviews_table(conn)