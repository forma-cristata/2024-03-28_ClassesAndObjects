class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        """Describes the restaurant's attributes in one sentence"""
        print(f"The restaurant is named {self.restaurant_name}, and serves {self.cuisine_type} food.")
    def open_restaurant(self):
        """Opens the restaurant and prints to the terminal"""
        print(f"{self.restaurant_name} is open.")
    def set_number_served(self, number):
        """Sets the initial number of people the restaurant has served"""
        print(f"{str(number)} people have been served here.")
        self.number_served = number
    def increment_number_served(self, other_number):
        """Increments the number of people the restaurant has served by the number that have been served today."""
        self.number_served += other_number
        print(f"{str(other_number)} people ate at {self.restaurant_name} today, totalling {self.number_served}.")
 
if __name__ == "__main__":        
    my_restaurant = Restaurant('Allen Street Grill', 'American')
    print(my_restaurant.restaurant_name)
    print(my_restaurant.cuisine_type)

    my_restaurant.describe_restaurant()
    my_restaurant.open_restaurant()

    #3
    this_restaurant = Restaurant('restaurant', 'food')
    print(this_restaurant.number_served)

    this_restaurant.set_number_served(100)
    this_restaurant.increment_number_served(14)

