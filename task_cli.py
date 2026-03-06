from typing import List, Optional


def display_main_menu() -> None:
    """Print the main menu options."""
    print("\n=== Task Manager ===")
    print("1) Add task")
    print("2) View tasks")
    print("3) Delete task")
    print("4) Quit")


def get_valid_menu_choice() -> Optional[int]:
    """Read and validate menu selection."""
    try:
        raw = input("Select an option (1-4): ").strip()
        choice = int(raw)
        if choice not in (1, 2, 3, 4):
            raise ValueError
    except ValueError:
        print("Error: Invalid menu option. Choose 1, 2, 3, or 4.")
        return None
    else:
        return choice
    finally:
        print("-" * 40)


def add_task(tasks: List[str]) -> None:
    """Add a task to the in-memory list."""
    try:
        task = input("Enter a task: ").strip()
        if not task:
            raise ValueError("Task cannot be empty.")
    except ValueError as err:
        print(f"Error: {err}")
    else:
        tasks.append(task)
        print(f'Added: "{task}"')
    finally:
        print("-" * 40)


def print_task_list(tasks: List[str]) -> None:
    """Print tasks with 1-based numbering."""
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def view_tasks(tasks: List[str]) -> None:
    """View all tasks or show empty-list warning."""
    try:
        if not tasks:
            raise LookupError("There are no tasks to view.")
    except LookupError as err:
        print(f"Notice: {err}")
    else:
        print("Current tasks:")
        print_task_list(tasks)
    finally:
        print("-" * 40)


def delete_task(tasks: List[str]) -> None:
    """Delete a task by selected index with validation."""
    try:
        if not tasks:
            raise LookupError("There are no tasks to delete.")

        print("Current tasks:")
        print_task_list(tasks)

        raw = input("Enter task number to delete: ").strip()
        index = int(raw) - 1

        if index < 0 or index >= len(tasks):
            raise IndexError("That task does not exist.")
    except ValueError:
        print("Error: Please enter a valid number.")
    except LookupError as err:
        print(f"Notice: {err}")
    except IndexError as err:
        print(f"Error: {err}")
    else:
        removed = tasks.pop(index)
        print(f'Deleted: "{removed}"')
    finally:
        print("-" * 40)


def run_task_manager() -> None:
    """Main CLI loop."""
    tasks: List[str] = []
    print("Welcome to the Task CLI!")

    try:
        while True:
            display_main_menu()
            choice = get_valid_menu_choice()

            if choice is None:
                continue
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                delete_task(tasks)
            elif choice == 4:
                print("Goodbye!")
                break
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
    else:
        print("Exited normally.")
    finally:
        print("Task CLI closed.")


if __name__ == "__main__":
    run_task_manager()