from dataclasses import dataclass, field
from typing import List
from datetime import date


@dataclass
class Task:
    title: str
    due_date: date
    completed: bool = False

    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True


@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet."""
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """Return all tasks for this pet."""
        return self.tasks


class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        """Add a pet."""
        self.pets.append(pet)

    def remove_pet(self, pet: Pet):
        """Remove a pet."""
        if pet in self.pets:
            self.pets.remove(pet)

    def get_pets(self) -> List[Pet]:
        """Return all pets."""
        return self.pets


class Scheduler:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """Add a task manually."""
        self.tasks.append(task)

    def get_tasks_for_day(self, day: date) -> List[Task]:
        """Filter tasks by date."""
        return [task for task in self.tasks if task.due_date == day]

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks."""
        return self.tasks
