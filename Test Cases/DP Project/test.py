# # import sys
# # import random
# # import time

# # sys.setrecursionlimit(1000)

# # def T(i, n, lengths):
# #     arr = [[0] * (n+1) for y in range(n+1)]

# #     for offset in range(0, n+1):
# #         for x in range(1, n+1):
# #             # x is i and y is j
# #             # gets the diagonals first
# #             y = x + offset
# #             if y <= n:
# #                 # Base cases
# #                 if x == y:
# #                     arr[x][y] = lengths[x]
# #                 elif y == (x + 1):
# #                     arr[x][y] = max(lengths[x], lengths[y])
# #                 else:
# #                     # Recursive case
# #                     arr[x][y] = max(lengths[x] + min(arr[x+2][y], arr[x+1][y-1]), lengths[y] + min(arr[x+1][y-1], arr[x][y-2]))

# #     # Return the result for the original problem
# #     return arr[i][n]


# # # START MAIN
# # i = 1
# # file1 = open(sys.argv[1], 'r')
# # Lines = file1.readlines()

# # # read first line
# # line1 = Lines[0].strip().split(' ')
# # line2 = Lines[1].strip().split(' ')

# # n = int(line1[0])
# # l = [0] * (n+1)

# # for k in range(1, n+1):
# #     l[k] = int(line2[k-1])

# # result = T(i, n, l)
# # print(result)


# # # def generate_random_array(n):
# # #     return [random.randint(1, 100) for _ in range(n)]

# # # n_values = [1, 2, 10, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100, 135, 500, 1000, 10000] 

# # # for n in n_values:
# # #     input_array = generate_random_array(n)
# # #     input_array.insert(0, 0)
# # #     start_time = time.time()
# # #     result = T(i, n, input_array)
# # #     end_time = time.time()
# # #     elapsed_time = end_time - start_time
# # #     print(f"n={n}, Runtime: {elapsed_time:.4f} seconds, Result: {result}")




# # import sys
# # import random
# # import time

# # sys.setrecursionlimit(10000)

# # dict = {}
# # def T(i, j, lengths):
# #     if (i, j) in dict:
# #         return dict[(i,j)]
# #     #base cases
# #     if (i==j):
# #         return lengths[i]

# #     if (j == (i+1)):
# #         return max(lengths[i], lengths[j])
    
# #     dict[(i,j)] = max(lengths[i] + min(T(i+2, j, lengths), T(i+1, j-1, lengths)), lengths[j] + min(T(i+1, j-1, lengths), T(i, j-2, lengths)))
    
# #     #recursive cases
# #     return dict[(i,j)]


# # #START MAIN
# # i = 1
# # file1 = open(sys.argv[1], 'r')
# # Lines = file1.readlines()

# # #read first line
# # line1 = Lines[0].strip().split(' ')
# # line2 = Lines[1].strip().split(' ')
 
# # n = int(line1[0])
# # l = [0] * (n+1)

# # for k in range(1, n+1):
# #     l[k] = int(line2[k-1])

# # print(T(i, n, l))

# # # def generate_random_array(n):
# # #     return [random.randint(1, 100) for _ in range(n)]

# # # n_values = [1, 2, 10, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100, 135, 500, 1000, 10000] 

# # # for n in n_values:
# # #     input_array = generate_random_array(n)
# # #     input_array.insert(0, 0)
# # #     start_time = time.time()
# # #     result = T(i, n, input_array)
# # #     end_time = time.time()
# # #     elapsed_time = end_time - start_time
# # #     print(f"n={n}, Runtime: {elapsed_time:.4f} seconds, Result: {result}")

# import sys
# import random
# import time

# sys.setrecursionlimit(100000)


# # def reconstruct_path(i, j, lengths, arr, steps,):
# #     memo = [["" for _ in range(n)] for _ in range(n)]
# #     if memo[i][j-1] != "":
# #         return memo[i][j]

# #     if i == j:
# #         memo[i][j] = str(i)
# #     elif j == (i + 1):
# #         memo[i][j] = str(i) + " " + str(j)
# #     elif lengths[i] + min(arr[i + 2][j], arr[i + 1][j - 1]) >= lengths[j] + min(arr[i + 1][j - 1], arr[i][j - 2]):
# #         memo[i][j] = str(i) + " " + str(reconstruct_path(i + 1, j, lengths, arr, steps))
# #     else:
# #         memo[i][j] = str(j) + " " + str(reconstruct_path(i, j - 1, lengths, arr, steps))

# #     return memo[i][j]

# def reconstruct_path(i, j, lengths, arr, steps):
#         if i == j:
#             return str(i)
#         elif j == (i + 1):
#             return str(i) + " " + str(j)
#         elif lengths[i] + min(arr[i+2][j], arr[i+1][j-1]) >= lengths[j] + min(arr[i+1][j-1], arr[i][j-2]):
#             return str(i) + " "  + str(reconstruct_path(i+1, j, lengths, arr, steps))
#         else:
#             return str(j) + " " + str(reconstruct_path(i, j-1, lengths, arr, steps))

# def T(i, n, lengths):
#     arr = [[0] * (n+1) for y in range(n+1)]
#     steps = [[""] * (n+1) for _ in range(n+1)]

#     for offset in range(0, n+1):
#         for x in range(1, n+1):
#             y = x + offset
#             if y <= n:
#                 if x == y:
#                     arr[x][y] = lengths[x]
#                 elif y == (x + 1):
#                     arr[x][y] = max(lengths[x], lengths[y])
#                 else:
#                     i_segment = lengths[x] + min(arr[x+2][y], arr[x+1][y-1])
#                     j_segment = lengths[y] + min(arr[x+1][y-1], arr[x][y-2])

#                     if  i_segment >= j_segment:
#                         arr[x][y] = i_segment
#                         steps[x][y] = reconstruct_path(x, y, lengths, arr, steps)
#                     else:
#                         arr[x][y] = j_segment
#                         steps[x][y] = reconstruct_path(x, y, lengths, arr, steps)

#     return arr[i][n], steps[i][n]


# i = 1
# file1 = open(sys.argv[1], 'r')
# Lines = file1.readlines()

# line1 = Lines[0].strip().split(' ')
# line2 = Lines[1].strip().split(' ')

# n = int(line1[0])
# l = [0] * (n+1)

# for k in range(1, n+1):
#     l[k] = int(line2[k-1])

# answer = T(i, n, l)
# cost = answer[0]
# traceback = answer[1]
# print(cost)
# print(traceback.strip())




# # def reconstruct_path(i, j, lengths, arr):
# #     if i == j:
# #         return str(i)
# #     elif j == (i + 1):
# #         return str(i) + " " + str(j)
# #     elif lengths[i] + min(arr[i+2][j], arr[i+1][j-1]) >= lengths[j] + min(arr[i+1][j-1], arr[i][j-2]):
# #         return str(i) + " " + str(reconstruct_path(i+1, j, lengths, arr))
# #     else:
# #         return str(j) + " " + str(reconstruct_path(i, j-1, lengths, arr))



# def generate_random_array(n):
#     return [random.randint(1, 100) for _ in range(n)]

# #n_values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] 
# n_values = [500, 2000]

# for n in n_values:
#     input_array = generate_random_array(n)
#     input_array.insert(0, 0)
#     start_time = time.time()
#     result, traceback = T(i, n, input_array)
#     end_time = time.time()
#     elapsed_time = end_time - start_time
#     print(f"n={n}, Runtime: {elapsed_time:.4f} seconds, Result: {result}")


import sys
import random
import time

# sys.setrecursionlimit(100000)

# traceback_dict = {}

# def reconstruct_path(i, j, lengths, arr):
#     if len(lengths) == 1:
#         return (i, None)
#     else:
#         if (i, j) in traceback_dict:
#             return traceback_dict[(i, j)]
        
#         if i == j:
#             return i, None
#         elif j == (i + 1):
#             if (lengths[i] >= lengths[j]):
#                 return (i, (j, None))
#             elif (lengths[j] > lengths[i]):
#                 return (j, (i, None))
            
#         elif lengths[i] + min(arr[i+2][j], arr[i+1][j-1]) >= lengths[j] + min(arr[i+1][j-1], arr[i][j-2]):
#             traceback_dict[(i, j)] = (i, reconstruct_path(i+1, j, lengths, arr))
#         else:
#             traceback_dict[(i, j)] = (j, reconstruct_path(i, j-1, lengths, arr))
        
#         return traceback_dict[(i, j)]


# def T(i, n, lengths):
#     arr = [[0] * (n+1) for y in range(n+1)]
#     steps = [[""] * (n+1) for y in range(n+1)]

#     for offset in range(0, n+1):
#         for x in range(1, n+1):
#             # x is i and y is j
#             # gets the diagonals first
#             y = x + offset
#             if y <= n:
#                 # Base cases
#                 if x == y:
#                     arr[x][y] = lengths[x]
#                     steps[x][y] = str(x)
#                 elif y == (x + 1):
#                     arr[x][y] = max(lengths[x], lengths[y])
#                     if (lengths[x] >= lengths[y]):
#                         steps[x][y] = str(x) + " " + str(y)
#                     elif (lengths[y] > lengths[x]):
#                         steps[x][y] = str(y) + " " + str(x)
#                 else:
#                     bottom_segment = lengths[x] + min(arr[x+2][y], arr[x+1][y-1])
#                     top_segment = lengths[y] + min(arr[x+1][y-1], arr[x][y-2])
#                     # Recursive case
#                     if bottom_segment >= top_segment:
#                         arr[x][y] = bottom_segment
#                         steps[x][y] = reconstruct_path(x, y, lengths, arr)
#                     else:
#                         arr[x][y] = top_segment
#                         steps[x][y] = reconstruct_path(x, y, lengths, arr)
                    

#     # Return the result for the original problem
#     return arr[i][n], steps[i][n]


# # START MAIN
# i = 1
# file1 = open(sys.argv[1], 'r')
# Lines = file1.readlines()

# # read first line
# line1 = Lines[0].strip().split(' ')
# line2 = Lines[1].strip().split(' ')

# n = int(line1[0])
# l = [0] * (n+1)

# for k in range(1, n+1):
#     l[k] = int(line2[k-1])

# answer = T(i, n, l)
# cost = answer[0]
# parse_arr = answer[1]


# traceback = ""
# if (n > 2) :
#     for i in range(0, n):
#         traceback += str(parse_arr[0]) + " "
#         parse_arr = parse_arr[1]

# else:
#     traceback = str(parse_arr)

# print(cost)
# print(traceback)


def generate_random_array(n):
    return [random.randint(1, 100) for _ in range(n)]

n_values = [100, 500, 1000, 2000] 
outputFile = open('outputfile_kruskal.txt', 'w')

for n in n_values:
    outputFile = open('input' + str(n) + '.txt', 'w')
    outputFile.write(str(n))
    outputFile.write('\n')
    input_array = generate_random_array(n)
    for num in input_array:
        outputFile.write(str(num) + " ")
    
    outputFile.close()

# for n in n_values:
#     input_array = generate_random_array(n)
#     input_array.insert(0, 0)
#     start_time = time.time()
#     result = T(i, n, input_array)
#     end_time = time.time()
#     elapsed_time = end_time - start_time
#     print(f"n={n}, Runtime: {elapsed_time:.4f} seconds, Result: {result}")