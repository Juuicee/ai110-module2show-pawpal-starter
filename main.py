from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import date

print("Running main.py...")

def main():
    # Create owner
    owner = Owner("Jordan")

    # Create pets
    dog = Pet("Mochi", "dog")
    cat = Pet("Luna", "cat")

    owner.add_pet(dog)
    owner.add_pet(cat)

    # Create tasks (same day for demo)
    task1 = Task("Morning walk", date.today())
    task2 = Task("Feed breakfast", date.today())
    task3 = Task("Vet visit", date.today())

    # Assign tasks to pets
    dog.add_task(task1)
    dog.add_task(task2)
    cat.add_task(task3)

    # Create scheduler
    scheduler = Scheduler()

    # IMPORTANT: manually load tasks into scheduler
    for pet in owner.get_pets():
        for task in pet.get_tasks():
            scheduler.add_task(task)

    # Print schedule
    print("\n--- Today's Schedule ---")

    today_tasks = scheduler.get_tasks_for_day(date.today())

    for task in today_tasks:
        status = "✅" if task.completed else "❌"
        print(f"{task.title} - {task.due_date} ({status})")


if __name__ == "__main__":
    main()