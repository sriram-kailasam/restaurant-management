import sqlite3
import os
from restaurants import RestaurantService, Restaurant

conn = sqlite3.connect(os.path.join(os.getcwd(), "restaurant.db"))

restaurant_service = restaurants.RestaurantService(conn)