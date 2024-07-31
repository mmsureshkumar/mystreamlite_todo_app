FILEPATH = "C:/Users/smurugas/OneDrive - Capgemini/Documents/Python/webapp1/todo.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file:
        return file.readlines()


def write_todos(todo_args, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todo_args)


if "__name__" == "__main":
    print("hello")
    print(get_todos(FILEPATH))
