def find_edges(dictionary, theseusR, theseusC, minotaurR, minotaurC, endR, endC, target):
    new_states = []
    original_state = (theseusR, theseusC, minotaurR, minotaurC)
  
    #base cases
    if(theseusR == minotaurR and theseusC == minotaurC):
        return
    elif((theseusR == endR and theseusC == endC) and (theseusR != minotaurR or theseusC != minotaurC)):
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

        not_visited_states = []
        
        for state in new_states:
            #if (state in visited_nodes):
            #    graph.add_edge(original_state, state)
            if (state not in visited_nodes):
                not_visited_states.append(state)


        for state in not_visited_states:
            visited_nodes.append(state)

        for state in not_visited_states:
            graph.add_edge(original_state, state)
            find_edges(dictionary, state[0], state[1], state[2], state[3], endR, endC, target)
        