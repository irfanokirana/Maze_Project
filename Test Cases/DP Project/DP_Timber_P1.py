import sys
import random
import time

def T(i, j, lengths):
    #base cases
    if (i==j):
        return lengths[i]

    if (j == (i+1)):
        return max(lengths[i], lengths[j])
    
    #recursive cases
    return max(lengths[i] + min(T(i+2, j, lengths), T(i+1, j-1, lengths)), lengths[j] + min(T(i+1, j-1, lengths), T(i, j-2, lengths)))

#START MAIN
i = 1
file1 = open(sys.argv[1], 'r')
Lines = file1.readlines()

#read first line
line1 = Lines[0].strip().split(' ')
line2 = Lines[1].strip().split(' ')
 
n = int(line1[0])
l = [0] * (n+1)

for k in range(1, n+1):
    l[k] = int(line2[k-1])

print(T(i, n, l))



# def generate_random_array(n):
#     return [random.randint(1, 100) for _ in range(n)]

# n_values = [5, 10, 15, 20, 25, 26, 27, 28] 

# for n in n_values:
#     input_array = generate_random_array(n)
#     input_array.insert(0, 0)
#     start_time = time.time()
#     result = T(i, n, input_array)
#     end_time = time.time()
#     elapsed_time = end_time - start_time
#     print(f"n={n}, Runtime: {elapsed_time:.4f} seconds, Result: {result}")

