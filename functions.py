filepath = 'todos.txt'
def get_todos(filepath=filepath):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos_arg, filepath = filepath):
    with open(filepath, 'w') as file:
        file.write(todos_arg)