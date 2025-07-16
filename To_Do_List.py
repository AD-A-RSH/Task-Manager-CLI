import json
import os
import sys
from colorama import Fore, Style

file_name = "todo.json"

def load_status():
    if not os.path.exists(file_name):
        return {'todo_list': []}
    with open(file_name, 'r') as file:
        return json.load(file)

def save_status(status):
    with open(file_name, 'w') as file:
        json.dump(status, file, indent=4)

def add_task(status):
    name = input("Enter your task :").title()
    state = False
    extra = input("You want to add any note (y/n) :").lower()
    if extra == 'y':
        note = input(f"Enter note for your {name} task :").title()
    elif extra == 'n':
        note = "None"
    else:
        print(Fore.RED + "Invalid choice, try again." + Style.RESET_ALL)
        return
    status['todo_list'].append({"TASK": name, "STATE": state, "NOTE": note})
    save_status(status)
    print(Fore.GREEN + "Task added!" + Style.RESET_ALL)

def view_task(status):
    if len(status['todo_list']) == 0:
        print(Fore.YELLOW + "\nNo tasks to show, so add some !!" + Style.RESET_ALL)
        sys.exit()
    else:
        for i, j in enumerate(status['todo_list']):
            task_state = "Pending" if j['STATE'] == False else "Completed"
            print(Fore.CYAN + f"{i+1}. {j['TASK']} | {j['NOTE']} | {task_state}\n" + Style.RESET_ALL)

def comp_incomp(status):
    view_task(status)
    number = int(input("Enter the number of the task you want to mark :"))
    which = int(input("Mark as 1. Completed or 2. Pending :"))
    if which == 1:
        status['todo_list'][number-1]['STATE'] = True
        print(Fore.GREEN + "Marked as Completed !" + Style.RESET_ALL)
    elif which == 2:
        status['todo_list'][number-1]['STATE'] = False
        print(Fore.YELLOW + "Marked as Pending !" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Invalid choice, try again." + Style.RESET_ALL)
        return
    save_status(status)

def edit(status):
    view_task(status)
    number = int(input("Enter the number of the task you want to edit :"))
    if number < 1 or number > len(status['todo_list']):
        print(Fore.RED + "Invalid number." + Style.RESET_ALL)
        return
    which = int(input("What you want to edit 1.Task\n2.Note :"))
    if which == 1:
        refined_task = input("Enter the refined task :").title()
        status['todo_list'][number-1]['TASK'] = refined_task
    elif which == 2:
        refined_note = input("Enter the refined note :").title()
        status['todo_list'][number-1]['NOTE'] = refined_note
    else:
        print(Fore.RED + "Invalid choice, try again !" + Style.RESET_ALL)
        return
    save_status(status)
    print(Fore.GREEN + "Updated Successfully" + Style.RESET_ALL)

def delete_task(status):
    view_task(status)
    number = int(input("Enter the number to delete :"))
    if number < 1 or number > len(status['todo_list']):
        print(Fore.RED + "Invalid number." + Style.RESET_ALL)
        return
    status['todo_list'].pop(number-1)
    save_status(status)
    print(Fore.GREEN + "Task deleted!" + Style.RESET_ALL)

def main():
    while True:
        status = load_status()
        print(Fore.MAGENTA + "Welcome to your To Do list manager !!!" + Style.RESET_ALL)
        print(Fore.YELLOW + "1. View Tasks\n2. Add Task\n3. Mark as complete/incomplete\n4. Edit a Specific Task\n5. Delete a task\n6. Quit" + Style.RESET_ALL)
        choice = int(input("Enter the number of your choice :"))
        if choice == 1:
            os.system("cls")
            view_task(status)
        elif choice == 2:
            add_task(status)
            input("Press Enter to continue...")
            os.system('cls')
        elif choice == 3:
            comp_incomp(status)
            input("Press Enter to continue...")
            os.system('cls')
        elif choice == 4:
            edit(status)
            input("Press Enter to continue...")
            os.system('cls')
        elif choice == 6:
            break
        elif choice == 5:
            delete_task(status)
            input("Press Enter to continue...")
            os.system('cls')
        else:
            print(Fore.RED + "Invalid choice, try again." + Style.RESET_ALL)
            input("Press Enter to continue...")
            os.system('cls')
main()
