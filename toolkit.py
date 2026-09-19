import random


# Tool 1: Number Guessing Game
# The user keeps guessing a secret number until they get it correct.
def number_guessing_game():
    print("\n--- Number Guessing Game ---")

    secret_number = random.randint(1, 10)
    attempts = 0

    print("I have chosen a number between 1 and 10.")

    while True:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("Please enter a whole number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(
                f"Congratulations! You guessed the number "
                f"{secret_number} in {attempts} attempts."
            )
            break


# Tool 2: To-Do List
# The user can add, view, and remove tasks from a changing list.
def todo_list():
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a task: ")
            tasks.append(task)
            print(f"Task '{task}' was added successfully.")

        elif choice == "2":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if not tasks:
                print("There are no tasks to remove.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                task_number = input("Enter the number of the task to remove: ")

                if task_number.isdigit():
                    task_number = int(task_number)

                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Task '{removed_task}' was removed.")
                    else:
                        print("That task number does not exist.")
                else:
                    print("Please enter a valid task number.")

        elif choice == "4":
            print("Returning to the main menu...")
            break

        else:
            print("Invalid choice. Please choose a number from 1 to 4.")


# Tool 3: Simple Calculator
# The user can perform basic arithmetic calculations.
def simple_calculator():
    print("\n--- Simple Calculator ---")

    first_number = input("Enter the first number: ")
    second_number = input("Enter the second number: ")

    try:
        first_number = float(first_number)
        second_number = float(second_number)
    except ValueError:
        print("Please enter valid numbers.")
        return

    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = input("Enter your choice: ")

    if operation == "1":
        result = first_number + second_number
        print(f"The result is {result}.")

    elif operation == "2":
        result = first_number - second_number
        print(f"The result is {result}.")

    elif operation == "3":
        result = first_number * second_number
        print(f"The result is {result}.")

    elif operation == "4":
        if second_number == 0:
            print("You cannot divide by zero.")
        else:
            result = first_number / second_number
            print(f"The result is {result}.")

    else:
        print("Invalid operation. Please choose 1, 2, 3, or 4.")


# Main menu
# This loop keeps the toolkit running until the user chooses Quit.
def main():
    print("\n========================================")
    print("       PERSONAL MINI-TOOLKIT")
    print("========================================")
    print("Welcome! Choose a tool below.")

    while True:
        print("\n1. Number Guessing Game")
        print("2. To-Do List")
        print("3. Simple Calculator")
        print("4. Quit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            number_guessing_game()

        elif choice == "2":
            todo_list()

        elif choice == "3":
            simple_calculator()

        elif choice == "4":
            print("\nThank you for using the Personal Mini-Toolkit!")
            print("Goodbye! Have a great day.")
            break

        else:
            print(
                f"'{choice}' is not a valid choice. "
                "Please choose 1, 2, 3, or 4."
            )


if __name__ == "__main__":
    main()