from pawpal_system import Task, Pet
from datetime import date


def test_mark_complete():
    task = Task("Test Task", date.today())
    task.mark_complete()
    assert task.completed is True


def test_add_task_to_pet():
    pet = Pet("Buddy", "dog")
    task = Task("Walk", date.today())

    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0].title == "Walk"