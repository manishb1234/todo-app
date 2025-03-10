#Read on Bitwise OR Operator

user_prompt = "Enter add or show or exit : "

todos=[]

while True:
  user_options = input(user_prompt)
  user_options = user_options.strip()
  match user_options :
      case 'add' :
          todo = input("Enter a todo item: ")
          todos.append(todo)
      case 'show' | 'display':
          #bitwise OR operator, so match with both show and display
          for index, item in enumerate(todos):
              item = item.title()
              print(index, '-', item)
    #for loop doesnt have arguments in ()
      case 'exit':
          break
      # entering a variable matches with any string except defined above
          #case whatever:
          #use case _ , a convention
      case _:
          print("You entered an unknown command")

print("Bye")
