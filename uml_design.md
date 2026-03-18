classDiagram
    class Owner {
        +name: str
        +pets: list[Pet]
        +add_pet()
        +remove_pet()
        +get_pets()
    }
    class Pet {
        +name: str
        +species: str
        +tasks: list[Task]
        +add_task()
        +get_tasks()
    }
    class Task {
        +title: str
        +due_date: date
        +completed: bool
        +mark_complete()
    }
    class Scheduler {
        +tasks: list[Task]
        +add_task()
        +get_tasks_for_day()
        +get_all_tasks()
    }
    Owner ||--o{ Pet : pets
    Pet ||--o{ Task : tasks
    Scheduler ||--o{ Task : tasks