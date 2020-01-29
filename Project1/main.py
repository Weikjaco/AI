from graph import Graph
from node import Node
from population_manager import PopulationManager
import json

def graphs_from_file():
    f = open("./graph.json", "r")
    j= f.read()
    y = json.loads(j)
    f.close()
    graph_list = []
    for graph in y:
        node_list = []
        for node in graph["nodes"]:
            node_list.append(Node(name= node[0],x=node[1],y=node[2],color="black"))
        graph_list.append(Graph(edges = graph["edges"], node_list = node_list))
    return graph_list

def write_graphs(graph_list):
    f = open("./graph.json", "w+")
    f.write("[")
    for i in graph_list:
        f.write("{")
        f.write('"nodes":[')
        nodes = i.nodes
        for j in nodes:
            f.write("["+str(j.name)+","+str(j.x)+","+str(j.y)+"]")
            if(j!=nodes[-1]):
                f.write(",")
        f.write("],\n")
        f.write('"edges":')
        f.write(str(i.edges).replace("(","[").replace(")","]"))
        f.write("}")
        if(i!=graph_list[-1]):
            f.write(",\n")

    f.write("]")
    f.close()

def generate_graphs():
    graph_list = []
    for i in range(10):
        g = Graph()
        g.gen_rand_graph(10*(i+1))
        graph_list.append(g)
    return graph_list

def main():
    # graph_list = generate_graphs()
    # write_graphs(graph_list)
    graph_list = graphs_from_file()
    #for i in graph_list:
    #    i.draw()

main()
