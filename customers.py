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
    
    def list_orders(self):
        q = """
            SELECT orders.id, restaurants.name, order.datetime
            FROM orders INNER JOIN restaurants
            ON orders.id = restaurants.id
        """

        c = self.conn.cursor()
        c.execute(q)

        rows = c.fetchall()
        print("Order ID\tRestaurant\tDate time")
        print("----------------------------------")
        for row in rows:
            print("%d\t%s\t%s" % (row[0], row[1], row[2]))