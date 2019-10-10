class RestaurantService:
    def __init__(self, conn):
        self.conn = conn

    def list_restaurants(self):
        q = """
            SELECT * FROM resturants;
        """

        c = self.conn.cursor()
        c.execute(q)

        rows = c.fetchall()

        for row in rows:
            print(row)

    def get_restaurant(self, id):
        q = """
            SELECT * FROM resturants WHERE id = ?;
        """

        c = self.conn.cursor()
        c.execute(q, (id, ))

        rows = c.fetchone()
        print(row)

    def create_restaurant(self, restaurant):
        q = """
            INSERT INTO restaurants VALUES (?, ?, ?);
        """

        try:
            c = self.conn.cursor()
            c.execute(q, (restaurant.id, restaurant.name, restaurant.address))

            print("Restaurant created")
        except Error as e:
            print(e)

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