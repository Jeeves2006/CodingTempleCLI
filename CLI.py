import os # statement imports the os module, provides functions for interacting with the operating system.

tasks = [] # empty list to store tasks, it will hold each task added by the user.

def clear_screen(): # clears the screen after each task.
    """Clear the terminal screen"""
os.system('cls' if os.name == 'nt' else 'clear') # clears the screen based on the operating system used.

def display_welcome_message():
    print("Welcome to the Task Manager CLI!") # displays welcome message.
    print("---------------------------------") # give the menu a little better look.

def display_menu():
    print("\nPlease choose an option:") # new line, prints out a simple menu. Asking the user to choose an option.
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

def add_task():
    task = input("Enter the task description: ") # asks user for input.
    tasks.append(task) # updates the list by adding the new task.
    print(f"Task '{task}' added successfully!") # confirms the task was added.

def view_tasks():
    if tasks: # checks if the lists contains any items. If true.
        print("\nYour tasks:")
    for idx, task in enumerate(tasks, 1): # starting the index from 1 instead of 0. This diplays the tasks with a numbered list.
        print(f"{idx}. {task}") # print index numebr and task.
    else:
        print("No tasks available.") # if false no tasks available.

def delete_task():
    if not tasks: # checks if the tasks list is empty, if true no tasks to delete displays.
        print("No tasks to delete.")
        return # exits the system after pressing return/enter.
    try: # handles errors that occur if the user puts in invalid number. 
        task_id = int(input("Enter the task number to delete: ")) # user input. select a number.
        if 1 <= task_id <= len(tasks): # this ensures the user enters a vaild task number. task_id starts the list with 1 to the lenght of the tasks list (4)
            deleted_task = tasks.pop(task_id - 1) # removes the task and stores it in deleted tasks, printing out the message below. 
            print(f"Task '{deleted_task}' deleted successfully!")
        else: # if false 
            print("invalid task number.")
    except ValueError: # catches non-numeric input, asking the user to enter a valid number.
        print("Please enter a valid number.")

def main(): # primary loop for running the CLI, keeps the program running.
    while True: # displays an infinite loop 
        clear_screen() 
        display_welcome_message()
        display_menu()

        try: # block to capture any error if the user enters anything other than an integer. 
            choice = int(input("\nEnter your choice: ")) # user input
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                delete_task()
            elif choice == 4:
                print("See Ya")
                break
            else:
                print("Invalid choice. Please select again.")
        except ValueError: # catches non-numeric input, asking the user to enter a valid number.
            print("please enter a valid numeber")
    input("\nPress Enter to continue...")

if __name__ == "__main__": # this condition is only true if the script is being directly. 
    main() # controls how the program runs and ensure that the main() function is only. 