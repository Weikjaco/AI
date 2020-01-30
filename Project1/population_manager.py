from graph import Graph

class PopulationManager:
    def __init__(self, pop_num, graph, col_list):
        self.pop_num = pop_num
        self.graph = graph
        self.col_list = col_list
        self.graph.edge_dict_setup()

    def search(self):
        #print(self.graph.edge_dict)

        stack = [self.graph.nodes[0].name]
        print(stack)
        def annealing_min_conflict(self):
        temp = 20000
        cooling_rate = .003
        best_state = self.graph  # We need to track our best state
        current_state = self.graph
        while temp > 1:
            # Get fitness of current state
            curr_energy = self.get_violations(current_state)
            print("Current Energy {}".format(curr_energy))
            # for i in range(len(best_state.nodes)):
            #     print(best_state.nodes[i].name, end=",")
            new_state = self.swap_nodes(current_state)
            new_energy = self.get_violations(new_state)
            print("New energy {}".format(new_energy))
            # If energy is better we accept the move
            if new_energy > curr_energy:
                current_state = new_state
            elif (math.e**(curr_energy-new_energy))/temp > rd.randrange(0,1):
                current_state = new_state
            # keep track of best solution
            if new_energy > self.get_violations(best_state):
                best_state = new_state
            # cool system
            temp *= 1-cooling_rate
            print(temp)
        print(best_state.edges)
        print(self.graph.edges)
        
    def get_violations(self, state):
        """Returns the number of violations within the current state"""
        num_violations = 0
        for edge in state.edges:
            for idx in range(1):
                # See if each edge consists of 2 nodes with same color
                if state.nodes[edge[idx]].color == state.nodes[edge[idx+1]].color:
                    num_violations += 1
        return num_violations

    def swap_nodes(self, state):
        """Swaps nodes within our current node list"""
        # Get nodes were swapping
        pos_one = rd.randint(0, len(state.nodes)-1)
        print(pos_one)
        pos_two = rd.randint(0, len(state.nodes)-1)

        # Stop them from being the same
        while pos_two == pos_one:
            pos_two = rd.randint(0, len(state.nodes)-1)
        print(pos_two)
        # Perform swap
        # print("Before Swap:")
        # for i in range(len(state.nodes)-1):
        #     print(state.nodes[i].name, end=",")
        temp = state.nodes[pos_one]
        state.nodes[pos_one] = state.nodes[pos_two]
        state.nodes[pos_two] = temp
        # print("\nAfter Swap")
        # for i in range(len(state.nodes)-1):
        #     print(state.nodes[i].name, end=",")

        new_state = state
        # print(new_state)
        return new_state
    
    def simple_backtracking(self):
        stack = [self.graph.nodes[0].name]
        curr = self.graph.get_node(stack[-1])
        curr.color = self.col_list[0]
        tried_color_stack = [[self.col_list[0]]]

        while(len(stack)!=len(self.graph.nodes) or violates(curr.name,self.graph)):
            #self.graph.draw()
            #check if current node violates its edges
            if(violates(curr.name,self.graph)):
                #print("violates")
                nxt_col = self.col_list.index(curr.color) + 1

                #if no more options, reset options and pop node from stack (change previous node)
                while(nxt_col == len(self.col_list)):
                    #reset this node
                    curr.color = "black"
                    stack = stack[:-1]
                    if (len(stack)==0):
                        print("no possible graph colorings")
                        break
                    tried_color_stack = tried_color_stack[:-1]
                    #move back to previous node
                    curr = self.graph.get_node(stack[-1])
                    nxt_col = self.col_list.index(curr.color) + 1
                if (len(stack)==0):
                    break
                #if yes, pick next color in color list
                curr.color = self.col_list[nxt_col]
                tried_color_stack[-1].append(self.col_list[nxt_col])


            #if no, pick the next edge in edge_dict
            else:
                added = False
                while(not added):
                    #print("doesn't violate")
                    for i in self.graph.edge_dict[curr.name]:
                        if i[0]==curr.name:
                            adj = i[1]
                        else:
                            adj = i[0]
                        if(adj not in stack):
                            stack.append(adj)
                            curr = self.graph.get_node(stack[-1])
                            curr.color = self.col_list[0]
                            tried_color_stack.append([self.col_list[0]])
                            added = True
                            break
                    if(not added):
                        curr_idx = stack.index(curr.name)
                        curr = self.graph.get_node(stack[curr_idx - 1])


                    #if no more edges, move back node and repeat
        self.graph.draw()

def violates(curr,graph):
    edge_list = graph.edge_dict[curr]
    color = graph.get_node(curr).color
    for i in edge_list:
        if i[0]==curr:
            adj = i[1]
        else:
            adj = i[0]
        adj_col = graph.get_node(adj).color
        if(adj_col == color):
            return True
    return False

