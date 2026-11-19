
import random

# Store tasks in a list while the program is running.
tasks = []


# TOOL 1: A calculator that performs basic arithmetic.
def calculator():
    print("\n--- SIMPLE CALCULATOR ---")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("Choose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        operation = input("Enter your choice (1-4): ")

        if operation == "1":
            result = num1 + num2
        elif operation == "2":
            result = num1 - num2
        elif operation == "3":
            result = num1 * num2
        elif operation == "4":
            if num2 == 0:
                print("You cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please choose 1-4.")
            return

        print(f"The answer is: {result}")

    except ValueError:
        print("Please enter valid numbers.")


# TOOL 2: A to-do list that allows users to manage tasks.
def todo_list():
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter your task: ").strip()

            if task:
                tasks.append(task)
                print(f"Task '{task}' added successfully!")
            else:
                print("Please enter a task.")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    task_number = int(input("Enter task number to remove: "))

                    if 1 <= task_number <= len(tasks):
                        removed = tasks.pop(task_number - 1)
                        print(f"Task '{removed}' removed successfully!")
                    else:
                        print("That task number does not exist.")

                except ValueError:
                    print("Please enter a valid task number.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print("Invalid choice. Please select 1-4.")


# TOOL 3: A guessing game that repeats until the correct answer.
def guessing_game():
    secret_number = random.randint(1, 10)
    attempts = 0

    print("\n--- NUMBER GUESSING GAME ---")
    print("I am thinking of a number between 1 and 10.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 10:
                print("Please guess a number between 1 and 10.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a whole number.")


# MAIN PROGRAM: Displays the menu and runs the selected tool.
def main():
    print("Welcome to My Personal Toolkit!")

    while True:
        print("\n===== MY PERSONAL TOOLKIT =====")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Number Guessing Game")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            calculator()

        elif choice == "2":
            todo_list()

        elif choice == "3":
            guessing_game()

        elif choice == "4":
            print("Thank you for using My Personal Toolkit. Goodbye!")
            break

        else:
            print(f"Sorry, '{choice}' is not a valid choice. Please select 1-4.")


# Start the program.
if __name__ == "__main__":
    main()
