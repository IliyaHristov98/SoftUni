from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    SERVICES = {"MainService": MainService, "SecondaryService": SecondaryService}
    ROBOTS = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type, name):
        if service_type not in self.SERVICES:
            raise Exception("Invalid service type!")

        self.services.append(self.SERVICES[service_type](name))
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type, name, kind, price):
        if robot_type not in self.ROBOTS:
            raise Exception("Invalid robot type!")

        self.robots.append(self.ROBOTS[robot_type](name, kind, price))
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name, service_name):
        robot = next(filter(lambda r: r.name == robot_name, self.robots))
        service = next(filter(lambda s: s.name == service_name, self.services))

        if robot.CONNECTION != service.CONNECTION:
            return "Unsuitable service."

        if service.capacity <= len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name, service_name):
        service = next(filter(lambda s: s.name == service_name, self.services))

        try:
            robot = next(filter(lambda r: r.name == robot_name, service.robots))
        except StopIteration:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name):
        service = next(filter(lambda s: s.name == service_name, self.services))

        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name):
        service = next(filter(lambda s: s.name == service_name, self.services))

        return f"The value of service {service_name} is {sum(robot.price for robot in service.robots):.2f}."

    def __str__(self):
        return "\n".join(r.details() for r in self.services)
