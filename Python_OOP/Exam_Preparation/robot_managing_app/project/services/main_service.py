from project.services.base_service import BaseService


class MainService(BaseService):
    CONNECTION = "MALE"

    def __init__(self, name):
        super().__init__(name, capacity=30)

    def details(self):
        return f"{self.name} Main Service:\n" \
               f"Robots: {' '.join(r.name for r in self.robots) if self.robots else 'none'}"
