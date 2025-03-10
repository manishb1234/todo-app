import json

with open("bonus15.json", 'r') as file:
    content = file.read() #reads content as string

data = json.loads(content)


for question in data: #iterate over a data list which is a list  of dictionaries
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(f"{index+1}-{alternative}")
    user_choice = int(input("Enter your answer: "))
    #recommended way is to inject that value in the current data structure
    question["user_choice"] = user_choice

score = 0
for index, question in enumerate(data):
    if question["correct_answer"] == question["user_choice"]:
        score = score + 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"

    message = f"{index + 1} {result} - Your Answer: {question['user_choice']}, " \
              f"Correct Answer: {question['correct_answer']}"
    print(message)

print("Score-", score, '/', len(data))

