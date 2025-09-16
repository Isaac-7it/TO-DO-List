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
        task = input('>>> Enter a task: ').lower()
        if task != '' and task not in tasks:
            tasks.append(task)
            print('>>> Task successfully added!')
        elif task in tasks:
            print('>>> Task has been added earlier!')
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
        task = input('>>> Enter the task to remove: ').lower()
        if task in tasks:
            tasks.remove(task)
    elif command == '4' or command == '4.' or command.lower() == 'exit':
        print('>>> Goodbye!')
        break

'''
- User should be able to keep on inputting task till 'done' is type
- If user should input an empty task, he should be reprompted with the task attribute only not the whole interface
- Users should be able to terminate or remove task using numbers 
'''