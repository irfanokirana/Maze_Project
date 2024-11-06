import networkx as nx
import sys

visited_nodes = []

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
    
def find_edges(dictionary, theseusR, theseusC, minotaurR, minotaurC, endR, endC, target):
    new_states = []
    original_state = (theseusR, theseusC, minotaurR, minotaurC)
    #if (original_state not in visited_nodes):
        #visited_nodes.append(original_state)
    

    #print("Original state:", original_state)
    #base cases
    if(theseusR == minotaurR and theseusC == minotaurC):
        print('Fail')
        return
    elif((theseusR == endR and theseusC == endC) and (theseusR != minotaurR or theseusC != minotaurC)):
        print('Success')
        graph.add_edge(original_state, target)
        return
    #recersive case
    else:
        
        #handle waiting node
        waiting_minotaur_pos1 = []
        waiting_minotaur_pos2 = []
        waiting_minotaur_pos1 = minotaur_move(dictionary, theseusR, theseusC, minotaurR, minotaurC)
        waiting_minotaur_pos2 = minotaur_move(dictionary, theseusR, theseusC, waiting_minotaur_pos1[0], waiting_minotaur_pos1[1])
        waiting_state = (theseusR, theseusC, waiting_minotaur_pos2[0], waiting_minotaur_pos2[1])
        print("waiting state:", waiting_state)
        new_states.append(waiting_state)

        #handle each direction node
        for direction in dictionary[(theseusR, theseusC)]:
            new_theseus_R = theseusR
            new_theseus_C = theseusC
            new_state = ()
            minotaur_position1 = []
            minotaur_position2 = []

            if direction == 'E':
                #theseus move
                new_theseus_C += 1
                #minotaur move in response to theseus (run algorithm twice)
                minotaur_position1 = minotaur_move(dictionary, new_theseus_R, new_theseus_C, minotaurR, minotaurC)
                minotaur_position2 = minotaur_move(dictionary, new_theseus_R, new_theseus_C, minotaur_position1[0], minotaur_position1[1])
                new_state = (new_theseus_R, new_theseus_C, minotaur_position2[0], minotaur_position2[1])
                new_states.append(new_state)
            if direction == 'W':
                new_theseus_C -= 1
                minotaur_position1 = minotaur_move(dictionary, new_theseus_R, new_theseus_C, minotaurR, minotaurC)
                minotaur_position2 = minotaur_move(dictionary, new_theseus_R, new_theseus_C, minotaur_position1[0], minotaur_position1[1])
                new_state = (new_theseus_R, new_theseus_C, minotaur_position2[0], minotaur_position2[1])
                new_states.append(new_state)
            if direction == 'S':
                new_theseus_R += 1
                minotaur_position1 = minotaur_move(dictionary, new_theseus_R, new_theseus_C, minotaurR, minotaurC)
                minotaur_position2 = minotaur_move(dictionary, new_theseus_R, new_theseus_C, minotaur_position1[0], minotaur_position1[1])
                new_state = (new_theseus_R, new_theseus_C, minotaur_position2[0], minotaur_position2[1])
                new_states.append(new_state)
            if direction == 'N':
                new_theseus_R -= 1
                minotaur_position1 = minotaur_move(dictionary, new_theseus_R, new_theseus_C, minotaurR, minotaurC)
                minotaur_position2 = minotaur_move(dictionary, new_theseus_R, new_theseus_C, minotaur_position1[0], minotaur_position1[1])
                new_state = (new_theseus_R, new_theseus_C, minotaur_position2[0], minotaur_position2[1])
                new_states.append(new_state)

        if (waiting_state == original_state):
            new_states.remove(waiting_state)


        #print("visited nodes")
        #print(set(visited_nodes))

        not_visited_states = []
        #print("all states")
        #print(new_states)
        for state in new_states:
            if (state in visited_nodes):
                graph.add_edge(original_state, state)
            if (state not in visited_nodes):
                not_visited_states.append(state)


        print("all states after removing visited ones")
        for state in not_visited_states:
            visited_nodes.append(state)
            print(state)

        #print('\n')
        for state in not_visited_states:
            graph.add_edge(original_state, state)
            #print('\n')
            print("Recursive state: ", state)
            find_edges(dictionary, state[0], state[1], state[2], state[3], endR, endC, target)
        
#if waiting state is equal to original state then continue
#read input
file1 = open(sys.argv[1], 'r')
Lines = file1.readlines()

line1 = Lines[0].strip().split(' ')
#read first line
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
#target node
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
                possible_states.append((i,j,k,l))
                
possible_states.append(target_node)

for i in range(0,len(possible_states)):
    graph.add_node((possible_states[i][0],possible_states[i][1],possible_states[i][2], possible_states[i][3]))


find_edges(board_dict, theseus_R, theseus_C, minotaur_R, minotaur_C, end_R, end_C, target_node)

#find shortest path
try:
    shortest_path = next(nx.all_shortest_paths(graph, source = starting_node, target = target_node, weight=None))
    #create output
    final_output = []

    for i in range(0, len(shortest_path) - 2):
        if (shortest_path[i][0] < shortest_path[i+1][0]):
            final_output.append('S')
        elif (shortest_path[i][0] > shortest_path[i+1][0]):
            final_output.append('N')
        elif (shortest_path[i][1] < shortest_path[i+1][1]):
            final_output.append('E')
        elif (shortest_path[i][1] > shortest_path[i+1][1]):
            final_output.append('W')
        elif ((shortest_path[i][0] == shortest_path[i+1][0]) and (shortest_path[i][1] == shortest_path[i+1][1])):
            final_output.append('X')

    #expected output for this is E
    for direction in final_output:
        print(direction, end=" ")
except:
    print("NO PATH")