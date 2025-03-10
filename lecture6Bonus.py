"""
Experiment 1
contents = ["All carrots are to be sliced "
            "longitudinally.",
            "The carrots were reportedly "
            "sliced",
            "The slicing process was well presented."]

names = ["doc.txt", "report.txt", "presentation.txt"]

for filename, content in zip(names,contents):
    file = open(f"files/{filename}",'w')
    file.write(content)
    file.close()"""


"""filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename  in filenames:
    file = open(filename, 'w')
    file.write('Hello')
    file.close()"""

#a.txt, b.txt, c.txt

"""filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(filename,'r')
    content = file.read()
    print(content)"""

file = open('logs.txt', 'w')
file.write('101.102.103.222 GET 01.988')
file.close()

file = open('logs.txt', 'w')
file.write('171.131.104.108 POST 2.143')
file.close()