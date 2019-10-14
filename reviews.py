class ReviewService:
    def __init__(self, conn):
        self.conn = conn

    def list_reviews(self):
        q = """
            SELECT restaurants.name, reviews.review, reviews.rating
            FROM reviews
            INNER JOIN restaurants 
            ON reviews.restaurant_id = restaurants.id
        """

        c = self.conn.cursor()
        c.execute(q)

        rows = c.fetchall()
        print("Restaurant\tReview\tRating")
        print("-----------------------------")
        for row in rows:
            print("%s\t%s\t%0.1f" % (row[0], row[1], row[2]))

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

class Review:
    def __init__(self, id, customer_id, restaurant_id, text, rating):
        self.id = id
        self.customer_id = customer_id
        self.restaurant_id = restaurant_id
        self.text = text
        self.rating = rating