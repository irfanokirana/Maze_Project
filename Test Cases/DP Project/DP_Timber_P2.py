import sys
import random
import time

sys.setrecursionlimit(100000)

def T(i, n, lengths):
    arr = [[0] * (n+1) for y in range(n+1)]

    for offset in range(0, n+1):
        for x in range(1, n+1):
            # x is i and y is j
            # gets the diagonals first
            y = x + offset
            if y <= n:
                # Base cases
                if x == y:
                    arr[x][y] = lengths[x]
                elif y == (x + 1):
                    arr[x][y] = max(lengths[x], lengths[y])
                else:
                    # Recursive case
                    arr[x][y] = max(lengths[x] + min(arr[x+2][y], arr[x+1][y-1]), lengths[y] + min(arr[x+1][y-1], arr[x][y-2]))

    # Return the result for the original problem
    return arr[i][n]


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

print(T(i, n, l))

def generate_random_array(n):
    return [random.randint(1, 100) for _ in range(n)]

n_values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 500, 1000, 2000] 

for n in n_values:
    input_array = generate_random_array(n)
    input_array.insert(0, 0)
    start_time = time.time()
    result = T(i, n, input_array)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"n={n}, Runtime: {elapsed_time:.4f} seconds, Result: {result}")


