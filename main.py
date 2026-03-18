from pawpal_system import Owner, Pet, Task, Scheduler
from datetime import date


def main():
    owner = Owner("Jordan")

    dog = Pet("Mochi", "dog")
    cat = Pet("Luna", "cat")

    owner.add_pet(dog)
    owner.add_pet(cat)

    # Tasks OUT OF ORDER (for sorting test)
    t1 = Task("Morning walk", date.today(), "09:00")
    t2 = Task("Feed breakfast", date.today(), "07:30")
    t3 = Task("Vet visit", date.today(), "09:00")  # conflict!

    dog.add_task(t1)
    dog.add_task(t2)
    cat.add_task(t3)

    scheduler = Scheduler()

    # Load tasks
    for pet in owner.get_pets():
        for task in pet.get_tasks():
            scheduler.add_task(task)

    print("\n--- Sorted Schedule ---")
    sorted_tasks = scheduler.sort_by_time(scheduler.get_all_tasks())

    for task in sorted_tasks:
        print(f"{task.time} - {task.title}")

    print("\n--- Incomplete Tasks ---")
    for task in scheduler.filter_by_status(False):
        print(task.title)

    print("\n--- Conflict Check ---")
    conflicts = scheduler.detect_conflicts()

    for c in conflicts:
        print(c)


if __name__ == "__main__":
    main()

# Used co-pilot to generate the above code based on the class definitions in pawpal_system.py. This is just a demo to show how the classes could be used together.