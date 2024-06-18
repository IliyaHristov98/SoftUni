class Class:

    def __init__(self, name, max_students=22):
        self.name = name
        self.students = []
        self.grades = []
        self.__students_count = max_students

    def add_student(self, name: str, grade: float):
        if len(self.students) < self.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        average_grade = sum(self.grades) / len(self.students)
        return round(average_grade, 2)

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade()}"
