from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):

    def __init__(self, brand, model, license_plate_number):
        super().__init__(brand, model, license_plate_number, max_mileage=180.0)

    def drive(self, mileage):
        self.battery_level -= (round(mileage / self.max_mileage * 100) + 5)

