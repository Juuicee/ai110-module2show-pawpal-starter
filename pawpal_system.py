from dataclasses import dataclass, field
from typing import List
from datetime import date


@dataclass
class Task:
    title: str
    due_date: date
    completed: bool = False

    def mark_complete(self):
        pass


@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        pass

    def get_tasks(self) -> List[Task]:
        pass


class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        pass

    def remove_pet(self, pet: Pet):
        pass

    def get_pets(self) -> List[Pet]:
        pass


class Scheduler:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        pass

    def get_tasks_for_day(self, day: date) -> List[Task]:
        pass

    def get_all_tasks(self) -> List[Task]:
        pass
