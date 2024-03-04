class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {type(animal).__name__} added to the zoo"

        if self.__budget < price:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = 0
        for worker in self.workers:
            total_salaries += worker.salary

        if total_salaries <= self.__budget:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_money_needed = 0
        for animal in self.animals:
            total_money_needed += animal.money_for_care

        if total_money_needed <= self.__budget:
            self.__budget -= total_money_needed
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals"
        count_of_types = {"Lion": [], "Tiger": [], "Cheetah": []}

        for animal in self.animals:
            count_of_types[type(animal).__name__].append(animal)

        for animal_type, data in count_of_types.items():
            result += f"\n----- {len(data)} {animal_type}s:"

            for instance in data:
                result += f"\n{instance}"

        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers"
        count_of_types = {"Keeper": [], "Caretaker": [], "Vet": []}

        for worker in self.workers:
            count_of_types[type(worker).__name__].append(worker)

        for worker_type, data in count_of_types.items():
            result += f"\n----- {len(data)} {worker_type}s:"

            for instance in data:
                result += f"\n{instance}"

        return result
