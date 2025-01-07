todos = []

while True:
    user_action = input('Please type add, show or exit: ')

    match user_action:
        case 'add':
            todo = input('Please type a todo: ')
            todos.append(todo)
        case 'show':
            print('Here is a list of your todos:')
            for item in todos:
                print(item)
        case 'exit':
            break

print('Bye!')