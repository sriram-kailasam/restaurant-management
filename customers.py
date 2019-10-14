from reviews import Review

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
            SELECT restaurants.name, reviews.review, reviews.rating
            FROM reviews
            INNER JOIN restaurants 
            ON reviews.restaurant_id = restaurants.id
            AND reviews.customer_id = ?
        """

        c = self.conn.cursor()
        c.execute(q, (id, ))

        rows = c.fetchall()
        print("Restaurant\tReview\tRating")
        print("-----------------------------")
        for row in rows:
            print("%s\t%s\t%0.1f" % (row[0], row[1], row[2]))

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

