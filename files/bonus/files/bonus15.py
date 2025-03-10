#quiz app
que1 = "What are dolphins?"
options1 = ["Amphibians", "Fish", "Mammals", "Birds"]
correct_option1 = 3

print(que1)
for name in options1:
    print(f"{options1.index(name)+1}-{name}")

user_answer1 = int(input("Enter your answer:"))

que2 = "What occupies most of the earth's surface?"
options2 = ["Land", "Water"]
correct_option2 = 2

print(que2)
for name in options2:
    print(f"{options2.index(name)+1}-{name}")

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


