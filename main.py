import sqlite3
import os
from restaurants import RestaurantService, Restaurant

conn = sqlite3.connect(os.path.join(os.getcwd(), "restaurant.db"))

while True:
    print("What do you want to look at?")
    print("1. Restaurants")
    print("2. Customers")
    print("3. Reviews")
    print("4. Exit")

    inp = int(input())

    if inp == 1:
        service = RestaurantService(conn)

        print("1. See all restaurants")
        print("2. Find restaurant by id")
        print("3. Create new restaurant")

        opt = int(input())

        if opt == 1:
            service.list_restaurants()
        elif opt == 2:
            id = int(input("Enter restaurant id: "))
            service.get_restaurant(id)
        elif opt == 3:
            id = int(input("Enter restaurant id: "))
            name = raw_input("Enter restaurant name: ")
            address = raw_input("Enter restaurant address: ")

            restaurant = Restaurant(id, name, address)
            service.create_restaurant(restaurant)
        else:
            print("Please select one from the given options.")

    elif inp == 2:
        pass
    elif inp == 3:
        pass 
    elif inp == 4:
        exit()
    else:
        print("Please select one from the given options.")
        continue