todos = []

while True:
    user_action = input('Please type add or show: ')

    match user_action:
        case 'add':
            todo = input('Please type a todo: ')
            todos.append(todo)
        case 'show':
            print(todos)

# user_action should be part of the while loop.
# If user_action is moved out of the while loop block,
# we create an infinite loop.