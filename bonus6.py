newMember = input("Add a new member:")

file = open("members.txt",'r')
content = file.readlines()
file.close()


content.append(newMember + "\n")
file = open("members.txt",'w')
content = file.writelines(content)
file.close()

