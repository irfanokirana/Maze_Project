import sys
import random
import time

sys.setrecursionlimit(100000)

traceback_dict = {}

def reconstruct_path(i, j, lengths, arr):
    if len(lengths) == 1:
        return (i, None)
    else:
        if (i, j) in traceback_dict:
            return traceback_dict[(i, j)]
        
        if i == j:
            return i, None
        elif j == (i + 1):
            if (lengths[i] >= lengths[j]):
                return (i, (j, None))
            elif (lengths[j] > lengths[i]):
                return (j, (i, None))
            
        elif lengths[i] + min(arr[i+2][j], arr[i+1][j-1]) >= lengths[j] + min(arr[i+1][j-1], arr[i][j-2]):
            traceback_dict[(i, j)] = (i, reconstruct_path(i+1, j, lengths, arr))
        else:
            traceback_dict[(i, j)] = (j, reconstruct_path(i, j-1, lengths, arr))
        
        return traceback_dict[(i, j)]


def T(i, n, lengths):
    arr = [[0] * (n+1) for y in range(n+1)]
    steps = [[""] * (n+1) for y in range(n+1)]

    for offset in range(0, n+1):
        for x in range(1, n+1):
            # x is i and y is j
            # gets the diagonals first
            y = x + offset
            if y <= n:
                # Base cases
                if x == y:
                    arr[x][y] = lengths[x]
                    steps[x][y] = str(x)
                elif y == (x + 1):
                    arr[x][y] = max(lengths[x], lengths[y])
                    if (lengths[x] >= lengths[y]):
                        steps[x][y] = str(x) + " " + str(y)
                    elif (lengths[y] > lengths[x]):
                        steps[x][y] = str(y) + " " + str(x)
                else:
                    bottom_segment = lengths[x] + min(arr[x+2][y], arr[x+1][y-1])
                    top_segment = lengths[y] + min(arr[x+1][y-1], arr[x][y-2])
                    # Recursive case
                    if bottom_segment >= top_segment:
                        arr[x][y] = bottom_segment
                        steps[x][y] = reconstruct_path(x, y, lengths, arr)
                    else:
                        arr[x][y] = top_segment
                        steps[x][y] = reconstruct_path(x, y, lengths, arr)
                    
    # Return the result for the original problem
    return arr[i][n], steps[i][n]


# START MAIN
i = 1
file1 = open(sys.argv[1], 'r')
Lines = file1.readlines()

# read first line
line1 = Lines[0].strip().split(' ')
line2 = Lines[1].strip().split(' ')

n = int(line1[0])
l = [0] * (n+1)

for k in range(1, n+1):
    l[k] = int(line2[k-1])

answer = T(i, n, l)
cost = answer[0]
parse_arr = answer[1]

print(parse_arr)


traceback = ""
if (n > 2) :
    for i in range(0, n):
        traceback += str(parse_arr[0]) + " "
        parse_arr = parse_arr[1]

else:
    traceback = str(parse_arr)

print(cost)
print(traceback)
