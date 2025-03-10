waiting_list = ["sen", "ben", "john"]
waiting_list.sort() #lists are mutable so list methods will mutate the list and wouldnt return anything
                    #strings are immutable so string methods will return a new string as they wont mutate the original string.
print(type(waiting_list.sort()))



'''Create a program with following output
   1.Ben
   2.John
   3.Sen
'''
'''
Algo - Given a list of 3 items, iterate over each item and print, that gives normal name.
to add index, use enumerate function with f strings
capitalize each item in iteration.

Sort them alphabetically, either a method (better) or take 2 items, take first two adn then compare and then shift position (basically implement sort method)
'''

for index, name in enumerate(waiting_list):
    print(f"{index+1}.{name.capitalize()}")

