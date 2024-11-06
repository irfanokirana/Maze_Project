import networkx as nx
import sys

#handles minotaur move
def minotaur_move(dictionary, theseusR, theseusC, minotaurR, minotaurC):
    minotaur_pos = [minotaurR, minotaurC]
    theseus_pos = [theseusR, theseusC]

    if(minotaur_pos == theseus_pos):
        return minotaur_pos
    #check if minotaur can move horizontally
    if (theseusC < minotaurC ):
        if 'W' in dictionary[(minotaurR, minotaurC)]:
            minotaur_pos[1] = minotaurC - 1
            return minotaur_pos
    elif (theseusC > minotaurC):
        if 'E' in dictionary[(minotaurR, minotaurC)]:
            minotaur_pos[1] = minotaurC + 1
            return minotaur_pos

    #check if minotaur can move vertically
    if (theseusR < minotaurR ):
        if 'N' in dictionary[(minotaurR, minotaurC)]:
            minotaur_pos[0] = minotaurR - 1
        else:
            return minotaur_pos
    elif (theseusR > minotaurR):
        if 'S' in dictionary[(minotaurR, minotaurC)]:
            minotaur_pos[0] = minotaurR + 1
        else:
            return minotaur_pos
    
    return minotaur_pos

#handles theseus move
def theseus_move(direction, theseusR, theseusC):
        new_theseus_pos = []
        new_theseus_R = theseusR
        new_theseus_C = theseusC

        if direction == 'E':
            new_theseus_C += 1
            new_theseus_pos = [new_theseus_R, new_theseus_C]
        elif direction == 'W':
            new_theseus_C -= 1
            new_theseus_pos = [new_theseus_R, new_theseus_C]
        elif direction == 'S':
            new_theseus_R += 1
            new_theseus_pos = [new_theseus_R, new_theseus_C]
        elif direction == 'N':
            new_theseus_R -= 1
            new_theseus_pos = [new_theseus_R, new_theseus_C]
        elif direction == '-':
            new_theseus_pos = [new_theseus_R, new_theseus_C]
        
        return new_theseus_pos

#read input
file1 = open(sys.argv[1], 'r')
Lines = file1.readlines()

#read first line
line1 = Lines[0].strip().split(' ')
rowCount = int(line1[0])
colCount = int(line1[1])
theseus_R = int(line1[2])
theseus_C = int(line1[3])
minotaur_R = int(line1[4])
minotaur_C = int(line1[5])
end_R = int(line1[6])
end_C = int(line1[7])

#starting node is (TR, TC, MR, MC)
starting_node = (theseus_R, theseus_C, minotaur_R, minotaur_C)
#target node, all paths point to exit node
target_node = 'EXIT'

#dictionary to hold valid directions for each space
board_dict = {}

for i in range (0, rowCount):
    row = Lines[i+1].strip().split(' ')
    for j in range (0, colCount):
        board_dict[(i+1,j+1)] = row[j]

graph = nx.DiGraph()
possible_states = []

# get all possible nodes/states
for i in range(1, rowCount+1):
    for j in range(1, colCount+1):
        for k in range (1, rowCount+1):
            for l in range(1, colCount+1):
                graph.add_node((i,j,k,l))
                
all_nodes = list(graph.nodes())

#get all edges
for node in all_nodes:
    if node != ('E', 'X', 'I', 'T'):
        next_moves = []
        #handle each direction
        for direction in board_dict[(node[0], node[1])]:
            new_theseus_pos = theseus_move(direction, node[0], node[1])
            new_minotaur_pos1 = minotaur_move(board_dict, new_theseus_pos[0], new_theseus_pos[1], node[2], node[3])
            new_minotaur_pos2 = minotaur_move(board_dict, new_theseus_pos[0], new_theseus_pos[1], new_minotaur_pos1[0], new_minotaur_pos1[1])
            next_moves.append((new_theseus_pos[0], new_theseus_pos[1], new_minotaur_pos2[0], new_minotaur_pos2[1]))
        #handle waiting
        new_theseus_pos = theseus_move('-', node[0], node[1])
        new_minotaur_pos1 = minotaur_move(board_dict, new_theseus_pos[0], new_theseus_pos[1], node[2], node[3])
        new_minotaur_pos2 = minotaur_move(board_dict, new_theseus_pos[0], new_theseus_pos[1], new_minotaur_pos1[0], new_minotaur_pos1[1])
        next_moves.append((new_theseus_pos[0], new_theseus_pos[1], new_minotaur_pos2[0], new_minotaur_pos2[1]))
        
        for move in next_moves:
            if((move[0] == end_R and move[1] == end_C) and (move[0] != move[2] or move[1] != move[3])):
                graph.add_edge(move, target_node)
                graph.add_edge(node, move)
            else:
                graph.add_edge(node, move)

#find shortest path
try:
    shortest_path = next(nx.all_shortest_paths(graph, source = starting_node, target = 'EXIT', weight=None))

    #sort all shortest paths 
    all_outputs = []
    for p in nx.all_shortest_paths(graph, source = starting_node, target = 'EXIT', weight=None):
        output = ""
        for i in range(0, len(p) - 2):
            if (p[i][1] < p[i+1][1]):
                output += 'E'
            elif (p[i][0] < p[i+1][0]):
                output += 'S'
            elif (p[i][0] > p[i+1][0]):
                output += 'N'
            elif (p[i][1] > p[i+1][1]):
                output += 'W'
            elif ((p[i][0] == p[i+1][0]) and (p[i][1] == p[i+1][1])):
                output += 'X'
        all_outputs.append(output)

    all_outputs.sort()

    #create final output
    final_output = all_outputs[0]

    for direction in final_output:
        print(direction, end=" ")
except:
    print("NO PATH")