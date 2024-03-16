from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VEH_TYPES = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name, last_name, driving_license_number):
        try:
            next(filter(lambda u: u.driving_license_number == driving_license_number, self.users))
            return f"{driving_license_number} has already been registered to our platform."
        except StopIteration:
            self.users.append(User(first_name, last_name, driving_license_number))
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type, brand, model, license_plate_number):
        if vehicle_type not in self.VEH_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        try:
            next(filter(lambda v: v.license_plate_number == license_plate_number, self.vehicles))
            return f"{license_plate_number} belongs to another vehicle."
        except StopIteration:
            self.vehicles.append(self.VEH_TYPES[vehicle_type](brand, model, license_plate_number))
            return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point, end_point, length):
        try:
            route = next(filter(lambda r: r.start_point == start_point and r.end_point == end_point, self.routes))
            if route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."

            if route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."

            if route.length > length:
                route.is_locked = True
        except StopIteration:
            pass

        self.routes.append(Route(start_point, end_point, length, len(self.routes) + 1))
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number, license_plate_number, route_id, is_accident_happened):
        user = next(filter(lambda u: u.driving_license_number == driving_license_number, self.users))
        route = next(filter(lambda r: r.route_id == route_id, self.routes))
        vehicle = next(filter(lambda v: v.license_plate_number == license_plate_number, self.vehicles))

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count):
        repaired = 0

        damaged_vehicles = filter(lambda x: x.is_damaged, self.vehicles)
        sorted_vehicles = sorted(damaged_vehicles, key=lambda x: (x.brand, x.model))

        try:
            for i in range(count):
                sorted_vehicles[i].change_status()
                sorted_vehicles[i].recharge()
                repaired += 1
        except IndexError:
            pass

        return f"{repaired} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda x: -x.rating)

        result = ["*** E-Drive-Rent ***"]

        for user in sorted_users:
            result.append(str(user))

        return "\n".join(result)
