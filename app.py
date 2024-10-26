def task():
    tasks = [] # Initialize an empty list to store tasks
    print("Welcome to the Task Manager ")
    total_task = int(input("Enter the number of task you wants to add = "))
    for i in range(1, total_task+1):
        task_name = input(f"Enter the task name {i} = ")
        tasks.append (task_name)
    print("Today tasks are \n{task}")

    while True:
        try:
            operations = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/stop/"))    
            if operations == 1 :
                add = input("Enter the number of task you wants to add")
                tasks.append(add)
                print(f"Task {add} is Added sucessfully")


            elif operations == 2 :
                update_val = input("Enter the task name you need to update = ")
                if update_val in tasks:
                    up = input("enter the new task = ")
                    ind = tasks.index(update_val)
                    tasks[ind] = up
                    print(f"Updated task '{updated_val}' to '{up}'.")
                else :
                    print("task not found")
            elif operations == 3: 
                Delete_val = input('Enter tha task you wants to delete = ')
                if Delete_val in tasks :
                    ind = tasks.index(Delete_val)
                    del tasks[ind] 
                    print(f'Your Task {Delete_val} is successfully Delted')
                else:
                    print ("task not found")

            elif operations == 4:
                print(f"Total task = {tasks}")
            elif operations == 5:
                print("closing the app")
                break

            else :
                print("Invalid input ")
        except ValueError:
            print("Invalid input please try again")
task()
    





