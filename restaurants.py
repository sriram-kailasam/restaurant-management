class RestaurantService:
    def __init__(self, conn):
        self.conn = conn

    def list_restaurants(self):
        q = """
            SELECT * FROM restaurants
        """

        c = self.conn.cursor()
        c.execute(q)

        rows = c.fetchall()

        print("Restaurants")
        print("---------------")

        for row in rows:
            print("%d. %s, %s" % (row[0], row[1], row[2]))

    def get_restaurant(self, id):
        q = """
            SELECT * FROM restaurants WHERE id = ?
        """

        c = self.conn.cursor()
        c.execute(q, (id, ))

        row = c.fetchone()
        if row is None:
            print("Restaurant not found")
        else:
            print("%d. %s, %s" % (row[0], row[1], row[2]))

    def create_restaurant(self, restaurant):
        q = """
            INSERT INTO restaurants VALUES (?, ?, ?)
        """

        try:
            c = self.conn.cursor()
            c.execute(q, (restaurant.id, restaurant.name, restaurant.address))
            
            self.conn.commit()
            print("Restaurant created")
        except Exception as e:
            print(e)

    def list_items(self, id):
        q = """
            SELECT name, price FROM items WHERE restaurant_id = ?
        """

        c = self.conn.cursor()
        c.execute(q, (id, ))

        rows = c.fetchall()
        
        print("Menu")
        print("-------")
        print("Name\tPrice")
        for row in rows:
            print("%s\t%0.2f" % (row[0], row[1]))

    def get_avg_rating(self, id):
        q = """
            SELECT AVG(rating) FROM reviews 
            GROUP BY restaurant_id 
            HAVING restaurant_id = ?
        """

        c = self.conn.cursor()
        c.execute(q, (id, ))

        row = c.fetchone()
        print(row)

    def get_total_revenue(self, id):
        pass
        

class Restaurant:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address