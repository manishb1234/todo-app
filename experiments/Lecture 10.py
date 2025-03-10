def greet():
    message = "hello"
    new_message = message.capitalize()
    return new_message

greeting = greet()
#Function call is  equal to its value. The value  is whatever is returned in the return message
print(greeting)
