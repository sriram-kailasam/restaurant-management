class CustomerService:
    def __init__(self, conn):
        self.conn = conn

    def list_customers(self):
        q = """
            SELECT * FROM customers
        """

        c = self.conn.cursor()
        c.execute(q)

        rows = c.fetchall()

        print("Customers")
        print("---------------")

        for row in rows:
            print("%d. %s, %d, %s" % (row[0], row[1], row[2], row[3]))

    def get_customer(self, id):
        q = """
            SELECT * FROM customers WHERE id = ?
        """

        c = self.conn.cursor()
        c.execute(q, (id, ))

        row = c.fetchone()
        if row is None:
            print("Customer not found")
        else:
            print("%d. %s, %d, %s" % (row[0], row[1], row[2], row[3]))
    
    def list_orders(self, id):
        q = """
            SELECT orders.id, restaurants.name, order.datetime
            FROM orders INNER JOIN restaurants
            ON orders.id = restaurants.id AND orders.customer_id = ?
        """

        c = self.conn.cursor()
        c.execute(q, (id, ))

        rows = c.fetchall()
        print("Order ID\tRestaurant\tDate time")
        print("----------------------------------")
        for row in rows:
            print("%d\t%s\t%s" % (row[0], row[1], row[2]))

    def list_reviews(self, id):
        q = """
            SELECT * FROM reviews WHERE customer_id = ?
        """

        c = self.conn.cursor()
        c.execute(q, (id, ))

        rows = c.fetchall()
        for (row in rows):
            print(row)

    def create_customer(self, customer):
        q = """
            INSERT INTO customers VALUES (?, ?, ?, ?)
        """

        try:
            c = self.conn.cursor()
            c.execute(q, (customer.id, customer.name, customer.age, customer.gender))
            
            self.conn.commit()
            print("Customer created")
        except Exception as e:
            print(e)

    def add_review(self, review):
        q = """
            INSERT INTO reviews VALUES (?, ?, ?, ?, ?)
        """

         try:
            c = self.conn.cursor()
            c.execute(q, (review.id, review.restaurant_id, review.customer_id, review.text, review.rating))
            
            self.conn.commit()
            print("Added review")
        except Exception as e:
            print(e)

class Customer:
    def __init__(self, id, name, age, gender):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender

class Review:
    def __init__(self, id, customer_id, restaurant_id, text, rating):
        self.id = id
        self.customer_id = customer_id
        self.restaurant_id = restaurant_id
        self.text = text
        self.rating = rating