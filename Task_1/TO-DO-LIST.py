def to_do_list():
    tasks = []

    def add():
        task = input("Enter the task: ").strip()
        tasks.append(task)
        print(f"Task '{task}' added.")

    def view():
        if not tasks:
            print("No tasks in the list.")
        else:
            print(tasks)

    def remove():
        print(tasks)
        task = input("Enter the task to remove: ").strip()
        if task in tasks:
            tasks.remove(task)
            print(f"Task '{task}' removed.")
        else:
            print("Task not found.")
    
    while True:
        print()
        print()
        choice = int(input("What do you want to do:\n1)add\n2)view\n3)remove\n4)exit\n: ").lower())
        
        if choice == 4 :
            print("Quitting the program...")
            break
        elif choice == 1:
            add()
        elif choice == 2:
            view()
        elif choice == 3:
            remove()
        else:
            print("Wrong Choice, Try agaain")
print("\nWelcome to TO-Do List")
to_do_list()
