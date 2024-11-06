import networkx as nx
import sys

file1 = open('input27.txt', 'r')
Lines = file1.readlines()

line1 = Lines[0].strip().split(' ')
num_vertices = line1[0]
num_edges = line1[1]
num_required = line1[2]

required_vertices = Lines[1].strip().split(' ')

graph = nx.Graph()

for i in range (1,int(num_vertices)):
    graph.add_node(int(i))

for i in range(2, len(Lines)-1):
    line = Lines[i].strip().split(' ')
    graph.add_edge(int(line[0]), int(line[1]), weight=int(line[2]))

MST = nx.minimum_spanning_tree(graph, weight='weight', algorithm='kruskal', ignore_nan=False)

edges = MST.edges(data=True)
total_edges = 0

for edge in edges:
    total_edges += 1

#generate output

outputFile = open('outputfile_kruskal_modified.txt', 'w')

outputFile.write(str(int(MST.size(weight='weight'))))
outputFile.write('\n')
outputFile.write(str(MST.number_of_edges()))
outputFile.write('\n')
for edge in edges:  
    outputFile.write(str(edge[0]) + " " + str(edge[1]))
    outputFile.write('\n')

outputFile.close()