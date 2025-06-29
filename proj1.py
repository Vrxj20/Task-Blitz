# Simple To-Do List App

tasks = []  # Store all tasks here

def add_task():
    task_name = input("Enter your task: ")
    tasks.append(task_name)
    print("Task has been added!!")

def list_task():
    for index, task in enumerate(tasks, start= 1):
        print(f"{index}. {task}")
    
    if tasks == []:
        print("List is empty")


def update_task():
    list_task()
    index = int(input("Enter the Task.no You want to UPDATE:  "))
    if 1 <= index <= len(tasks):
        new_task = input("Enter new Task:  ")
        tasks[index] = new_task
    else:
        print("Invalid Task.no")



def delete_task():
    list_task()
    index = int(input("Enter the Task.no You want to DELETE:  "))
    if 1 <= index <= len(tasks):
        tasks.pop(index)
        print("The task has been succesfully removed. You can view your new To-do list by typing '2' !! ")
    

def main():

    while True:
        print("\n To do List App    ||    Select Option")
        print("1.Add a Task in the list:  ")
        print("2.List all the Tasks:  ")
        print("3.Update Task List:  ")
        print("4.Delete a task:  ")
        print("5.Exit the app:  ")
        choice = input("Choose an option: ")

        match choice:
            case '1':
                add_task()
            case '2':
                list_task()
            case '3':
                update_task()
            case '4':
                delete_task()
            case '5':
                break
            case _:
                print("Invalid choice")
                
if __name__ == "__main__":
    main()
