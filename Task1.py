import os
from tkinter.tix import InputOnly
def display_menu():
    print(f"To-Do List Application")
    print("1) View To-Do List")
    print("2) Add Task")
    print("3) Mark as Completed Task")
    print("4) Clear Tasks")
    print("5) Exit")

def view_tasks():
    if os.path.exists("Task.txt"):
        with open("Task.txt","r") as file:
            tasks=file.read().splitlines()
            if tasks:
                for i,task in enumerate(tasks):
                    print(f"{i+1}.{task}")
            else:
                print("No task")
    else:
        print("No List found.Create new")

def add_task():
    task=input("Enter Task:")
    with open("Task.txt","a") as file:
        file.write(task+"\n")
    print(f"'{task}' Added.")

def mark_completed():
    view_tasks()
    task_num = int(input("Enter task number to be Marked as Complete:") )-1
    with open("Task.txt","r") as file:
        tasks=file.read().splitlines()
        if 0<=task_num<len(tasks):
            completed_task=tasks.pop(task_num)
            with open("Task.txt","w") as file:
                file.write("\n".join(tasks))
            with open("Completed.txt","a") as completed_file:
                completed_file.write(completed_task+"\n")
            print(f"Task {completed_task}'Mark as Completed.")
        else:
            print("Invalid")
def clear_completed_tasks():
    if os.path.exists("completed.txt"):
        with open("completed.txt","r") as completed_file:
            completed_tasks=completed_file.read().splitlines()
        with open("completed.txt","w") as completed_file:
            completed_file.write("")
        print("Completed Task Clear.")
    else:
        print("No Task to clear.")
if __name__=="__main__":
    while True:
        display_menu()
        choice=input("Enter the Choice(1/2/3/4/5): ")
        
        if choice =="1":
            view_tasks()
        elif choice =="2":
            add_task()
        elif choice =="3":
            mark_completed()
        elif choice =="4":
            clear_completed_tasks()
        elif choice =="5":
            break
        else:
            print("Invalid.Please Re-Enter.")
            if _name_ == "_main_":
                main()
