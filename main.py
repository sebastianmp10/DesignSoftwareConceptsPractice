import string
import random

class VehiculoInfo:
    brand: str
    catalogue_price: int
    electric: bool

    def __init__(self, brand, electric, catalogue_price):
        self.brand = brand
        self.electric = electric
        self.catalogue_price = catalogue_price

    def compute_tax(self):
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02
        return tax_percentage * self.catalogue_price

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Payable tax: {self.compute_tax()}")

class Vehiculo:
    id: str
    license_plate: str
    info: VehiculoInfo

    def __init__(self, id, license_plate, info):
        self.id = id
        self.license_plate = license_plate
        self.info = info

    def print(self):
        print(f"ID: {self.id}")
        print(f"License plate: {self.license_plate}")
        self.info.print()

class RegistroVehiculo:

    vehicle_info = {}

    def add_vehicle_info(self, brand, electric, catalogue_price):
        self.vehicle_info[brand] = VehiculoInfo(brand, electric, catalogue_price)

    def __init__(self):
        self.add_vehicle_info("Tesla Model 3", True, 60000)
        self.add_vehicle_info("Volkswagen ID3", True, 35000)
        self.add_vehicle_info("BMW 5", False, 45000)
        self.add_vehicle_info("Tesla Model Y", True, 75000)

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self, brand):
        vehicle_id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license(vehicle_id)
        return Vehiculo(vehicle_id, license_plate, self.vehicle_info[brand])

class Aplicacion:

    def register_vehicle(self, brand: string):
        #Create a registry instance
        registry = RegistroVehiculo()

        #create a vehicle
        return registry.create_vehicle(brand)


app = Aplicacion()
vehicle = app.register_vehicle("Tesla Model Y")
vehicle.print()