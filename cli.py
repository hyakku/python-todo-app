import functions
import time

now = time.strftime("%b %d %Y %H:%M:%S")
print("The time is below: ")
print(f"The current date and time is {now}")


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index+1}-{item.capitalize()}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            index = number - 1

            todos = functions.get_todos()


            existing_todo = todos[index]
            print ("The existing item on your todo list at number " + str(index+1) + " is " + existing_todo)
            new_todo = input("Enter new todo: ")
            todos[index] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            index = number - 1

            todos = functions.get_todos()

            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            print (f"Todo {todo_to_remove} was removed from the list")

        except IndexError:
            print ("That doesn't correspond with a remaining todo.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print ("Command is not valid.")

print ("Bye!")

