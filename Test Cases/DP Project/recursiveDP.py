import sys
import random
import time

cuts = []

fileName = sys.argv[1]

f = open(fileName, "r")

numSegmentsStr = f.readline()
numSegmentsInt = int(numSegmentsStr)

cutsLine = f.readline()
cutsStr = cutsLine.split()
for x in range(numSegmentsInt):
    cuts.append(int(cutsStr[x]))

f.close()

T = []

#table_start = time.time()
print(cuts)

for i in range(len(cuts)):
    tList = []
    for j in range(len(cuts)):
        tList2 = []
        tList2.append(-1)
        tList2.append([])
        tList.append(tList2)
    T.append(tList)

#print(T)

#print("Table TTE: ", time.time() - table_start)

#numCalls = [0]

#program_start = time.time()

for i in range(len(cuts) - 1):
    T[i][i][0] = cuts[i]
    T[i][i][1].append(i + 1)
    if(cuts[i] >= cuts[i+1]):
        T[i][i+1][0] = cuts[i]
        T[i][i+1][1].append(i+1)
        T[i][i+1][1].append(i+2)
    else:
        T[i][i+1][0] = cuts[i+1]
        T[i][i+1][1].append(i+2)
        T[i][i+1][1].append(i+1)

T[len(cuts) - 1][len(cuts) - 1][0] = cuts[len(cuts)-1]
T[len(cuts) - 1][len(cuts) - 1][1].append(len(cuts))



def cutting(i, j): 
    if(j == i): 
        return T[i][i][0]
    if(j == i + 1): 
        return T[i][j][0]
    
    option1 = 0
    option2 = 0
    option3 = 0

    if(T[i+2][j][0] != -1):
        #already exists
        option1 = T[i+2][j][0]
    else:
        option1 = cutting(i + 2, j)

    if(T[i + 1][j - 1][0] != -1):
        #already exists
        option2 = T[i+1][j-1][0]
    else:
        option2 = cutting(i + 1, j - 1)

    if(T[i][j - 2][0] != -1):
        #already exists
        option3 = T[i][j - 2][0]
    else:
        option3 = cutting(i, j - 2)
    
    if(cuts[i] + min(option1, option2) >= cuts[j] + min(option2, option3)):
        if(option1 > option2):
            #choose option 2
            #we went left, they went right
            T[i][j][0] = cuts[i] + option2
            T[i][j][1].append(i+1)
            T[i][j][1].append(j+1)
            T[i][j][1].extend(T[i+1][j-1][1])
            return cuts[i] + option2
        else:
            #choose option 1
            #we went left, they went left
            T[i][j][0] = cuts[i] + option1
            T[i][j][1].append(i+1)
            T[i][j][1].append(i+2)
            T[i][j][1].extend(T[i+2][j][1])
            return cuts[i] + option1
    else:
        if(option2 > option3):
            #choose option 3
            #we both went right
            T[i][j][0] = cuts[j] + option3
            T[i][j][1].append(j+1)
            T[i][j][1].append(j)
            T[i][j][1].extend(T[i][j-2][1])
            return cuts[j] + option3
        else:
            #choose option 2
            #we went right, they went left
            T[i][j][0] = cuts[j] + option2
            T[i][j][1].append(j+1)
            T[i][j][1].append(i+1)
            T[i][j][1].extend(T[i+1][j-1][1])
            return cuts[j] + option2



cutting(0, len(cuts) - 1)
moves = ""
if(T[0][len(cuts)-1][0] == -1):
    print("0")
else:
    print(T[0][len(cuts)-1][0])

for x in T[0][len(cuts)-1][1]:
    moves += str(x) + " "
print(moves.strip())

