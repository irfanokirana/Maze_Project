import networkx as nx



#algobowl verifier

output = open('output_from_677_to_677.txt', 'r')
output_lines = output.readlines()

input = open('input_group677.txt', 'r')
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


#check if the graph is connected
if (nx.is_connected(output_graph)):
    print("CONNECTED")
else:
    print("NOT CONNECTED")

#check that all required vertices are in the output graph
for node in required_vertices:
    if int(node) not in output_graph.nodes:
        print("MISSING REQUIRED NODE", node)

#check that the edges in output exist in our graph
sum = 0
for edge in output_graph.edges:
    sum += input_graph.get_edge_data(edge[0], edge[1])['weight']
    if (input_graph.get_edge_data(edge[0], edge[1]) is None):
        print("EDGE NOT FOUND")

if (int(sum) == int(total_cost)):
    print("COST IS VALID")
else:
    print("COST IS INVALID")
    print("EXPECTED COST:", sum)
    print("GIVEN COST:", total_cost)


#check for cycles
try:
    nx.find_cycle(output_graph, source=1, orientation=None)
    print("CYCLE FOUND")
except:
    print("NO CYCLE FOUND")







