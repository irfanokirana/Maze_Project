outputFile = open('sample_input.txt', 'w')

outputFile.write('1000 999 500')
outputFile.write('\n')
#write required edges
for i in range(1, 501):
    outputFile.write(str(i) + " ")
outputFile.write('\n')
#write edges
for i in range(1, 1000):  
    outputFile.write(str(i) + " " + str(i + 1) + " 1")
    outputFile.write('\n')

outputFile.close()