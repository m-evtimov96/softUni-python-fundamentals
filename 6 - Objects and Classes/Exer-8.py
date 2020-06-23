class Vehicle:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money, owner):
        if money > self.price and self.owner is None:
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {money - self.price:.2f}"
        elif owner is not None:
            return "Sorry, not enough money"
        elif owner is None:
            return "Car already sold"

    def sell(self):
        if self.owner is None:
            return "Vehicle has no owner"
        else:
            self.owner = None

    def __repr__(self):
        if self.owner is None:
            string_to_return = f"{self.model} {self.type} is on sale: {self.price}"
        else:
            string_to_return = f"{self.model} {self.type} is owned by: {self.owner}"
        return string_to_return


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
print(vehicle.sell())
print(vehicle)

# fix this