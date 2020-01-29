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
