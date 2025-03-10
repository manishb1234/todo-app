#program to get temperatures from a text file and calculate and print the average of these values

def get_average():

    #extract data from data.txt

    with open("files/data.txt", 'r') as file:
        data = file.readlines() #have intermediate variables, reading in one line and slicing in other line

    values = data[1:]
    values = [float(i) for i in values]

    average_local = sum(values)/len(values)
    return average_local

average = get_average()
print(average)
