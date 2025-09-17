running = True
tasks = []

print('''---TO-DO LIST---
1. Add Task
2. View Task
3. Remove Task
4. Exit''')
while running:
    command = input('>>> Choose an option: ')
    if command == '1' or command == '1.' or command.lower() == 'add':
        # Multi task adding
        adding_task = True
        while adding_task:
            task = input('>>> Enter a task (Type done after adding task(s)): ').lower()
            if task.lower() != 'done':
                if task != '' and task not in tasks:
                    tasks.append(task)
                elif task in tasks:
                    print('>>> Task has been added earlier!')
                elif task == '':
                    print('>>> Kindly input a task')
            elif task.lower() == 'done':
                print('>>> Task(s) successfully added!')
                adding_task = False
    elif command == '2' or command == '2.' or command.lower() == 'view':
        if len(tasks) != 0:
            counter = 1
            print('>>> Your task(s) are: ')
            for task in tasks:
                print(f'{counter}. {task.capitalize()}')
                counter += 1
        else:
            print(f">>> Nothing to show! Use the 'add' command to add task(s)")
    elif command == '3' or command == '3.' or command.lower() == 'remove':
        if len(tasks) > 0:
            #task removed using the task itself
            '''task = input('>>> Enter the task to remove: ').lower()
            if task in tasks:
                tasks.remove(task)
                print('Task removed successfully!')
            else:
                print('>>> Task not found!')'''
            # Task removed using task number
            task_number = int(input('>>> Enter the task number to remove: '))
            if 0 < task_number <= len(tasks):
                tasks.remove(tasks[task_number - 1])
                print('>>> Task removed successfully!')
            else:
                print('Error - Enter a valid task number')
        else:
            print(f">>> No added task! Use the 'add' command to add task(s)")
    elif command == '4' or command == '4.' or command.lower() == 'exit':
        print('>>> Goodbye!')
        break