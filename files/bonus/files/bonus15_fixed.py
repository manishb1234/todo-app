que1 = "What are dolphins?"
option1 = ["Amphibians", "Fish", "Mammals", "Birds"]

que2 = "What occupies most of the earth's surface?"
option2 = ["Land", "Water"]

correct_option = [3,2]

print(que1)

def entry(que,options,index):
    for name in options:
        print(f"{options.index(name) + 1}-{name}")
    user_answer_temp = int(input("Enter your answer:"))
    user_answer.append(user_answer)

entry(que1, option1)

print(que2)

entry(que2,option2)

user_answer2 = int(input("Enter your answer:"))

score = 0
if user_answer1 == correct_option1:
    print(f"1 Correct Answer: User Answer: {user_answer1}, Correct Answer: {correct_option1}")
    score = score+1
else:
    print(f"1 Incorrect Answer: User Answer: {user_answer1}, Correct Answer: {correct_option1}")

if user_answer2 == correct_option2:
    print(f"2 Correct Answer: User Answer: {user_answer2}, Correct Answer: {correct_option2}")
    score = score+1
else:
    print(f"2 Incorrect Answer: User Answer: {user_answer2}, Correct Answer: {correct_option2}")

print(f"Score:{score}/")