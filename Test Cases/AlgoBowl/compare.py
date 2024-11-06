# import networkx as nx

# output = open('output_modified707.txt', 'r')
# output_lines = output.readlines()

# file1 = open('input_group707.txt', 'r')
# Lines = file1.readlines()

# line1 = Lines[0].strip().split(' ')
# num_vertices = line1[0]
# num_edges = line1[1]
# num_required = line1[2]

# required_vertices = Lines[1].strip().split(' ')

# graph = nx.Graph()

# for i in range (1,int(num_vertices)+1):
#     graph.add_node(int(i))

# for i in range(2, len(Lines)):
#     line = Lines[i].strip().split(' ')
#     graph.add_edge(int(line[0]), int(line[1]), weight=int(line[2]))

# nodes_to_remove = {}
# for node in graph.nodes:
#     if str(node) not in required_vertices:
#         this_edges = []
#         connecting_nodes = []
#         for edge in graph.edges:
#             if ((int(node) == edge[0])):
#                 this_edges.append(edge)
#                 if (str(edge[1]) in required_vertices):
#                     connecting_nodes.append(edge[1])
#             elif ((int(node) == edge[1])):
#                 this_edges.append(edge)
#                 if (str(edge[0]) in required_vertices):
#                     connecting_nodes.append(edge[0])

#         if (len(connecting_nodes) <= 1):
#             nodes_to_remove[node] = this_edges
    
    
# #print(nodes_to_remove)
# for node in nodes_to_remove:
#     graph.remove_node(node)
#     if ((not nx.is_connected(graph)) and (len(nodes_to_remove[node]) > 1)):
#             graph.add_node(node)
#             for edge in nodes_to_remove[node]:
#                 graph.add_edge(edge[0], edge[1])

# num_edges = 0
# sum = 0
# for edge in graph.edges:
#     num_edges += 1
#     #print(edge)

# #print("num edges:", num_edges)
# #print("cost:", graph.size(weight='weight'))


# #output graph
# output_graph = nx.Graph()

# total_cost = int(output_lines[0].strip())
# num_edges = int(output_lines[1].strip())


# for i in range(2, len(output_lines)):
#     line = output_lines[i].strip().split(' ')
#     output_graph.add_edge(int(line[0]), int(line[1]))

# # count = 0
# # for edge2 in graph.edges:
# #     #print("got here")
# #     if (edge2 not in output_graph.edges):
# #         count+=1
# #         print(edge2)

# # print(num_edges-count)

# # edges_no_duplicates = []
# # for edge in output_graph:
# #     if edge not in edges_no_duplicates:
# #         edges_no_duplicates.append(edge)
# #     else:
# #         print("duplicate found")

# for edge in output_graph.edges:
#     print("Edge:", edge)
#     print("Weight:", graph[edge[0]][edge[1]]['weight'])
#     print('\n')

# print("Weight:", graph[90][95]["weight"])

import networkx as nx

#algobowl verifier

output = open('output_modified707.txt', 'r')
output_lines = output.readlines()

input = open('input_group707.txt', 'r')
input_lines = input.readlines()

#create output graph
output_graph = nx.Graph()

total_cost = int(output_lines[0].strip())
num_edges = int(output_lines[1].strip())


for i in range(2, len(output_lines)):
    line = output_lines[i].strip().split(' ')
    output_graph.add_edge(int(line[0]), int(line[1]))

#create input graph
input_graph = nx.Graph()

line1 = input_lines[0].strip().split(' ')
num_vertices = line1[0]
num_edges = line1[1]
num_required = line1[2]

required_vertices = input_lines[1].strip().split(' ')


for i in range (1,int(num_vertices)+1):
    input_graph.add_node(int(i))

for i in range(2, len(input_lines)):
    line = input_lines[i].strip().split(' ')\
    
    input_graph.add_edge(int(line[0]), int(line[1]), weight=int(line[2]))


#check that the edges in output exist in our graph
sum = 0
for edge in output_graph.edges:
    print("Edge:", edge)
    sum += input_graph.get_edge_data(edge[0], edge[1])['weight']


print(sum)


