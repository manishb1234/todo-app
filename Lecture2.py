user_prompt = "Enter a todo list: "

todos = []

while True:
    todo = input(user_prompt)
    todos.append(todo.title()) #title and capitalize change first letter to capital and forcefully convert other letters to lowercase
    print(todos)
