class Review:
    reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.reviews.append(self)

    # function that returns the rating for a restaurant.
    def rating(self):
        return self.rating

    # function that returns the customer object for that review
    def customer(self):
        return self.customer

    # function that returns the restaurant object for that given review
    def restaurant(self):
        return self.restaurant

    # function that returns all of the reviews
    def all():
        return Review.reviews



class Customer:
    customers = []

    def __init__(self, name, family_name):
        self.name = name
        self.family_name = family_name
        self.reviews = []
        Customer.customers.append(self)

    # function that returns the customer's given name
    def given_name(self):
        return self.name

    # function that returns the customer's famliy name
    def family_name(self):
        return self.family_name

    # function that returns the full name of the customer, with the given name and the family name
    def full_name(self):
        return f"{self.name} {self.family_name}"

    # return all of customers instances
    def all():
        return Customer.customers

    def restaurants(self):
        return list(set(review.restaurant() for review in self.reviews))

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)

    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, full_name):
        for customer in cls.customers:
            if customer.full_name() == full_name:
                return customer

    @classmethod
    def find_all_by_given_name(cls, given_name):
        return [customer for customer in cls.customers if customer.name == given_name]



class Restaurant:
    restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.restaurants.append(self)

    # function that returns the restaurant's name
    def name(self):
        return self.name

    # function that returns a list of all reviews for that restaurant
    def reviews(self):
        return self.reviews

    # function that Returns a **unique** list of all customers who have reviewed a particular restaurant.
    def customers(self):
        return list(set(review.customer() for review in self.reviews))

    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_ratings = sum(review.rating() for review in self.reviews)
        return total_ratings / len(self.reviews)

    def all():
        return Restaurant.restaurants




# Create customers
customer1 = Customer("Samuel", "Ngugi")
customer2 = Customer("Ashley", "Wanjiru")

# Create restaurants
restaurant1 = Restaurant("Nairobi Street Kitchen")
restaurant2 = Restaurant("KFC")

# Add reviews
customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant2, 3)
customer2.add_review(restaurant1, 5)

# Test class methods
found_customer = Customer.find_by_name("Samuel Ngugi")
print(found_customer.given_name())  # Output: "Samuel"


customers_with_given_name = Customer.find_all_by_given_name("Ashley")
for customer in customers_with_given_name:
    print(customer.full_name())  # Output: "Ashley Wanjiru"


# Test the total number of reviews by a customer
print(customer1.num_reviews())  # Output: 2

# Test for review data
reviews = Review.all()
for review in reviews:
    print(f"{review.customer.full_name()} reviewed {review.restaurant.name} with a rating of {review.rating}")
