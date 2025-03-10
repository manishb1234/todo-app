temperatures = [10,12,14]

file = open("file.txt",'w')

file.writelines([str(temperature)+'\n' for temperature in temperatures])

file.close()