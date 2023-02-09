import functions
import time

now_date = time.strftime("%d-%b-%Y  %H:%M")
print("It is", now_date)
while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        # file = open('db.txt', 'r')
        # todos = file.readlines()

        todos = functions.get_todos()

        todos.append(todo + '\n')
        functions.write_todos(todos)

    elif user_action.startswith('show'):
        # new_todos = []
        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)

        # new_todos = [item.strip('\n') for item in todos]

        # file = open('db.txt', 'r')
        # todos = file.readlines()
        # file.close()

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_t = input('New todo: ')
            todos[number] = new_t + '\n'

            functions.write_todos(todos)

        except ValueError:
            print('Your command is not valid!')
            continue

    elif user_action.startswith('exit'):
        break

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            todos_deleted = todos[number - 1]
            todos.pop(number - 1)
            functions.write_todos(todos)

            print(f"Todos was deleted: {todos_deleted}")

        except IndexError:
            print('There is no item whit that number.')
            continue

    else:
        print('Hey, you entered a unknown command.')

