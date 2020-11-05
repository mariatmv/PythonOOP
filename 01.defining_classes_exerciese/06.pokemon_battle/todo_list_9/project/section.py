class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name: str):
        if task_name not in self.tasks:
            return f'Could not find task with the name {task_name}'
        task_name.completed = not task_name.completed
        return f'Completed task {task_name}'

    def clean_section(self):
        completed_tasks = list(filter(lambda t: t.completed, self.tasks))
        if completed_tasks:
            for task in completed_tasks:
                self.tasks.remove(completed_tasks)
        return f'Cleared {len(completed_tasks)} tasks.'

    def view_section(self):
        output = f'Section {self.name}:'
        for t in self.tasks:
            output += '\n' + t.details()
        return output

