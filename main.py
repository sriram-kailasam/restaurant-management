import sqlite3
import os
from restaurants import RestaurantService, Restaurant
from customers import CustomerService, Customer
from reviews import Review, ReviewService

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
        print("4. See the menu")
        print("5. See Average rating")
        # print("6. See total revenue")

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
        elif opt == 4:
            id = int(input("Enter restaurant id: "))
            service.list_items(id)
        elif opt == 5:
            id = int(input("Enter restaurant id: "))
            service.get_avg_rating(id)
        # elif opt == 6:
        #     id = int(input("Enter restaurant id: "))
        #     service.get_total_revenue(id)

        else:
            print("Please select one from the given options.")

    elif inp == 2:
        service = CustomerService(conn)

        print("1. See all customers")
        print("2. Find customer by id")
        print("3. See all orders of a customer")
        print("4. Create new customer")
        print("5. See all reviews of customer")

        opt = int(input())
        if opt == 1:
            service.list_customers()
        elif opt == 2:
            id = int(input("Enter customer id: "))
            service.get_customer(id)
        elif opt == 3:
            id = int(input("Enter customer id: "))
            service.list_orders(id)
        elif opt == 4:
            id = int(input("Enter customer id: "))
            name = raw_input("Enter customer name: ")
            age = int(input("Enter customer age: "))
            gender = raw_input("Enter customer's gender: ")

            customer = Customer(id, name, age, gender)
            service.create_customer(customer)
        elif opt == 5:
            id = int(input("Enter customer id: "))
            service.list_reviews(id)
        else:
            print("Please select one from the given options.")
    elif inp == 3:
        service = ReviewService(conn)

        print("1. See all reviews")
        print("2. Add review")

        opt = int(input())
        if opt == 1:
            service.list_reviews()
        elif opt == 2:
            id = int(input("Enter review id: "))
            customer_id = int(input("Enter customer id: "))
            restaurant_id = int(input("Enter restaurant id: "))
            text = input("Enter review: ")
            rating = float(input("Enter rating (1-5)"))

            review = Review(id, customer_id, restaurant_id, text, rating)
            service.add_review(review)
        else:
            print("Please select one from the given options.")
    elif inp == 4:
        exit()
    else:
        print("Please select one from the given options.")
        continue