import uuid
class Car:

    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.id = uuid.uuid4()

    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Price: {self.price}"

class Dealership:

    def __init__(self, name):
        self.name = name
        self.car_inventory = {}

    # def add_car(self, car):
        
    #     if car.make in list(self.car_inventory.keys()):
    #         car_brand = self.car_inventory[car.make]

    #         if car_brand[car.model]:
    #             if car_brand[car.model][car.year]:
    #                 car_brand[car.model][car.year].append(car)
    #                 print(f"{car.make} {car.model} {car.year} model added in existing inventory")
    #                 return True
    #             else:
    #                 car_brand[car.model][car.year] = [car]
    #                 print(f"{car.make} {car.model} {car.year} model added by creating new year model in inventory")
    #                 return True
    #         else:
    #             car_brand[car.model] = {car.model : {car.year: [car]}}
    #             print(f"{car.make} {car.model} {car.year} model added by creating New Model inventory")

    #     else:
    #         self.car_inventory[car.make] = {car.model: {car.year: [car] } }
    #         print(f"{car.make} {car.model} {car.year} model added by creating New Brand / Make inventory")

    def add_car(self, car):
        # Set up a new make if it does not exist
        make_inventory = self.car_inventory.setdefault(car.make, {})
        
        # Set up a new model under the make if it does not exist
        model_inventory = make_inventory.setdefault(car.model, {})
        
        # Set up a new year entry for the model if it does not exist
        year_inventory = model_inventory.setdefault(car.year, [])
        
        # Append the car to the list for that specific year
        year_inventory.append(car)
        print(f"{car.make} {car.model} {car.year} model added to inventory.")


    def disply_car_inventory(self):
        # Printing inventory for readability
        for make, models in self.car_inventory.items():
            print(f"Make: {make}")
            for model, years in models.items():
                print(f"  Model: {model}")
                for year, cars in years.items():
                    print(f"    Year: {year} - {len(cars)} car(s)")
                    for car in cars:
                        print(f"      {car}")
                        print("-----------------------")
        print(self.car_inventory)

    def sell_car(self, car):
        self.cars.remove(car)
        pass


car1 = Car("Toyota", "Camry", 2020, 25000)

car2 = Car("Toyota", "Aqua", 2020, 25000)
car3 = Car("Toyota", "Aqua", 2021, 25000)
car4 = Car("Toyota", "Aqua", 2021, 25000)
car5 = Car("Honda", "Visel", 2021, 25000)


# car2 = Car("Honda", "Accord", 2019, 23000)

Moto = Dealership('MotoGP')

Moto.add_car(car1)
Moto.disply_car_inventory()
Moto.add_car(car2)
Moto.disply_car_inventory()
Moto.add_car(car3)
Moto.disply_car_inventory()
Moto.add_car(car4)
Moto.disply_car_inventory()
Moto.add_car(car5)
Moto.disply_car_inventory()

        