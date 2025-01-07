todos = []

while True:
    user_action = input('Please type ADD, SHOW, EDIT or EXIT: ')
    user_action = user_action.strip().upper()

    match user_action:
        case 'ADD':
            todo = input('Please type a todo: ')
            todo = todo.capitalize()
            todos.append(todo)
        case 'SHOW':
            print('Here is a list of your todos:')
            for i in range(len(todos)):
                print(i + 1, todos[i])
        case 'EDIT':
            i = int(input('Type the number of the todo to edit: '))
            temp_todo = todos[i - 1]
            new_item = input('Type the new todo: ')
            todos[i - 1] = new_item
            print('Previous name:', temp_todo, 'New name:', new_item)
        case 'EXIT':
            break

print('Bye!')