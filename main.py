import textwrap

def menu():
    menu = """
        MY TO-DO APP
        
        [+] Add task
        [-] Remove task
        [C] Done task
        [V] Review
        [q] Quit
        => """
    return input(textwrap.dedent(menu))

#
def add_task(tasks): #Adiciona a task (input) a lista de dicionários "tasks" (ordena uma lista não ordenada de chave-valor)
    task = input("Describe your task: ")
    tasks.append({"task": task, "done": False})
    print(f"Task '{task}' added.\n")

def remove_task(tasks):
    task_number = int(input("Enter the task number to remove: \n"))
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['task']}' removed.\n")
    else:
        print("Invalid task number.")

def done_task(tasks):
    task_number = int(input("Enter the task number to mark as done: \n"))
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        print(f"Task '{tasks[task_number - 1]['task']}' marked as done.\n")
    else:
        print("Invalid task number.")

def review_tasks(tasks):
    if not tasks:
        print("No tasks to show.\n")
    else:
        #enumera independente do estado da task: 2
        for index, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Not done"
            print(f"{index}. {task['task']} [{status}]")

def main():
    tasks = [] #lista de tasks
    
    while True:
        opcao = menu()
        if opcao == "+":
            add_task(tasks)
        elif opcao == "-":
            remove_task(tasks)
        elif opcao.upper() == "C":
            done_task(tasks)
        elif opcao.upper() == "V":
            review_tasks(tasks)
        elif opcao.lower() == "q":
            print("Quiting.")
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
