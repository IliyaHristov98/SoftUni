from task import Task


class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"

        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name):
        try:
            task = next(filter(lambda t: t.name == task_name, self.tasks))
        except StopIteration:
            return f"Could not find task with the name {task_name}"

        task.completed = True

        return f"Completed task {task_name}"

    def clean_section(self):
        number_of_tasks = 0
        for t in self.tasks[:]:
            if t.completed:
                self.tasks.remove(t)
                number_of_tasks += 1
        return f"Cleared {number_of_tasks} tasks."

    def view_section(self):
        tasks_with_details = "\n".join(t.details() for t in self.tasks)
        return f"Section {self.name}:\n{tasks_with_details}"
