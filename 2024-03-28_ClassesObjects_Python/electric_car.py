from cars import Car

class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery_size = 40
        self.battery = Battery()
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")
        
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()

my_leaf.fill_gas_tank()
my_leaf.battery.describe_battery()