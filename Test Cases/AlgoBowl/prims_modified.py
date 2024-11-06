import networkx as nx
from networkx.algorithms import tree
import sys



def remove_redundant_nodes(g_original: nx.Graph, terminal_nodes: list) -> nx.Graph:
    """
    Prune the Steiner Tree by removing the non-terminal nodes so that all the leaves
    are terminals

    :param g_original: the graph to be pruned
    :param terminal_nodes: list of terminal nodes of the graph that have to be connected by a steiner tree
    :return: pruned approximation of the optimal Steiner Tree
    """
    g = nx.Graph(g_original)

    # collecting all leaf non-terminal nodes
    leaf_non_terminal_nodes = [node for node in g.nodes() if g.degree(node) == 1 and node not in terminal_nodes]

    # retrace the chain of neighbors until a terminal node is encountered
    while leaf_non_terminal_nodes:
        for node in leaf_non_terminal_nodes[:]:
            neighbour = next(g.neighbors(node))  # get leaf neighbour

            g.remove_node(node)
            leaf_non_terminal_nodes.remove(node)

            if g.degree(neighbour) == 1 and neighbour not in terminal_nodes:  # check if it is a terminal
                leaf_non_terminal_nodes.append(neighbour)

    return g





#open file
file1 = open('input_group687.txt', 'r')
Lines = file1.readlines()

#get values
line1 = Lines[0].strip().split(' ')
num_vertices = line1[0]
num_edges = line1[1]
num_required = line1[2]

required_vertices = []
for terminal in Lines[1].strip().split(' '):
    required_vertices.append(int(terminal))



#create graph
graph = nx.Graph()

for i in range (1,int(num_vertices)+1):
    graph.add_node(int(i))

for i in range(2, len(Lines)):
    line = Lines[i].strip().split(' ')
    graph.add_edge(int(line[0]), int(line[1]), weight=int(line[2]))

#print("initial cost:", graph.size(weight='weight'))


# #check for leaf nodes
# nodes_to_remove = {}
# for node in graph.nodes:
#     #get all non terminal nodes
#     if str(node) not in required_vertices:
#         this_edges = []
#         connecting_nodes = []
#         #gets edges of nonterminal
#         for edge in graph.edges:
#             if ((int(node) == edge[0])):
#                 #keep track of all edges to add back in if removing the node will disconnect the graph
#                 this_edges.append((edge, graph.get_edge_data(edge[0], edge[1])['weight']))
#                 #check if an edge connects non terminal with terminal node
#                 if (str(edge[1]) in required_vertices):
#                     connecting_nodes.append(edge[1])
#             elif ((int(node) == edge[1])):
#                 this_edges.append((edge, graph.get_edge_data(edge[0], edge[1])['weight']))
#                 if (str(edge[0]) in required_vertices):
#                     connecting_nodes.append(edge[0])

#         #if the non terminal is conencted to one or less terminal, we can remove it
#         if (len(connecting_nodes) <= 1):
#             nodes_to_remove[node] = this_edges
    

#remove nodes.
# for node in nodes_to_remove:
#     graph.remove_node(node)
#     #check if removing the node disconnects the graph
#     #and (len(nodes_to_remove[node]) > 1)
#     if ((not nx.is_connected(graph))):
#             graph.add_node(node)
#             for edge in nodes_to_remove[node]:
#                 graph.add_edge(edge[0][0], edge[0][1], weight=int(edge[1]))



#generate minimum spanning tree


pruned_graph = remove_redundant_nodes(graph, required_vertices)

MST = nx.minimum_spanning_tree(pruned_graph, weight='weight', algorithm='prim', ignore_nan=False)

edges = MST.edges(data=True)

#generate output

outputFile = open('output_modified687.txt', 'w')

outputFile.write(str(int(MST.size(weight='weight'))))
outputFile.write('\n')
outputFile.write(str(MST.number_of_edges()))
outputFile.write('\n')
for edge in edges:  
    outputFile.write(str(edge[0]) + " " + str(edge[1]))
    outputFile.write('\n')

outputFile.close()