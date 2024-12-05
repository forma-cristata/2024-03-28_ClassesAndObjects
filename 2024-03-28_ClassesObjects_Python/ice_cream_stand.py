from restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    def display_flavors(self):
        """Prints the falvors available at the restaurant"""
        print(f"Available Ice Cream Flavors at {self.restaurant_name}: ", end="")
        for flavor in self.flavors:
            print(flavor.title(), end="\t")
            
if __name__ == "__main__":
    we_all_scream = IceCreamStand("The ice cream shop", "desserts", ['vanilla', 'chocolate', 'neopolitan', 'cookie dough', 'mint chip'])
    we_all_scream.display_flavors()