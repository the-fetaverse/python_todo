todos = []

while True:
    user_action = input('Please type ADD, SHOW or EXIT: ')
    user_action = user_action.strip().upper()

    match user_action:
        case 'ADD':
            todo = input('Please type a todo: ')
            todo = todo.capitalize()
            todos.append(todo)
        case 'SHOW':
            print('Here is a list of your todos:')
            for item in todos:
                print(item)
        case 'EXIT':
            break

print('Bye!')