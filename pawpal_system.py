from typing import List
from typing import List, Optional
from datetime import date, datetime, timedelta
from datetime import date, timedelta
from dataclasses import dataclass, field

# This file defines the core classes for the PawPal system: Owner, Pet, Task, and Scheduler. These classes will be used to manage pet care tasks and schedules.
@dataclass
class Task:
    title: str
    due_date: date
    time: str  # "HH:MM"
    completed: bool = False
    frequency: Optional[str] = None  # "daily", "weekly", or None

    def mark_complete(self):
        """Mark task complete and return next task if recurring."""
        self.completed = True

        if self.frequency == "daily":
            return Task(self.title, self.due_date + timedelta(days=1), self.time, False, "daily")

        if self.frequency == "weekly":
            return Task(self.title, self.due_date + timedelta(days=7), self.time, False, "weekly")

        return None


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

# In a real implementation, this would contain the scheduling logic to prioritize and order tasks based on constraints. For now, it just stores tasks and can filter them by date.  
    def get_tasks_for_day(self, day: date) -> List[Task]:
        """Filter tasks by date."""
        return [task for task in self.tasks if task.due_date == day]
# This method filters tasks based on a specific date.  It returns only tasks that match the given day.

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks."""
        return self.tasks
    from datetime import datetime

    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        """Return tasks sorted by time."""
        return sorted(tasks, key=lambda t: datetime.strptime(t.time, "%H:%M"))

    def filter_by_status(self, completed: bool) -> List[Task]:
        """Filter tasks by completion status."""
        return [t for t in self.tasks if t.completed == completed]

    def detect_conflicts(self) -> List[str]:
        """Detect tasks with same date and time."""
        warnings = []
        seen = {}

        for task in self.tasks:
            key = (task.due_date, task.time)

            if key in seen:
                warnings.append(
                    f"⚠ Conflict: '{task.title}' conflicts with '{seen[key].title}' at {task.time}"
                )
            else:
                seen[key] = task

        return warnings
# Used co-pilot to generate the above code based on the requirements for the PawPal system. This is just a starting point and can be expanded with more features and logic as needed.