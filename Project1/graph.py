from node import Node

import turtle
import random

UPPER_DOMAIN = 100

class Graph:
    def __init__(self, edges=[],node_list=[]):
        self.nodes = node_list
        self.edges = edges

    def __str__(self):
        return str(self.edges)

    def get_node(self, name):
        for i in self.nodes:
            if i.name == name:
                return i

    def gen_rand_graph(self, node_num):
        self.nodes = []
        self.edges = []

        idx = 0
        invalid_xy = []
        while(idx<node_num):
            x = random.randrange(0,UPPER_DOMAIN)
            y = random.randrange(0,UPPER_DOMAIN)
            n = Node(name = idx,x=x,y=y,color="black")
            if((x,y) not in invalid_xy):
                invalid_xy.append((x,y))
                self.nodes.append(n)
                idx+=1

        #queue defines the list of nodes that still can have edges added to them
        queue = self.nodes
        while len(queue) != 1:
            #print(len(queue))
            curr = queue[0]
            poss_nodes = queue[1:].copy()
            while(len(poss_nodes) != 0):
                closest, idx = find_nearest(curr, poss_nodes)
                if(not self.edge_crossed(curr, closest) and ((curr.name,closest.name) not in self.edges and (closest.name,curr.name) not in self.edges)):
                    self.edges.append((curr.name,closest.name))
                    break
                poss_nodes = poss_nodes[:idx] + poss_nodes[idx+1:]

            #if there are no possible edges left, pop this node from our queue
            if(len(poss_nodes) == 0):
                queue = queue[1:]
            random.shuffle(queue)

    def edge_dict_setup(self):
        self.edge_dict = {}
        for key in self.nodes:
            self.edge_dict.update({key.name:[]})

        for edge in self.edges:
            self.edge_dict[edge[0]].append(edge)
            self.edge_dict[edge[1]].append(edge)

    #TODO need more explanation:
    def edge_crossed(self, n1, n2):
        for i in self.edges:
            e1 = self.get_node(i[0])
            e2 = self.get_node(i[1])
            if(self.cross(n1, n2, e1, e2)):
                return True
        return False
    def cross(self, p1,p2,p3,p4):
        if(p1==p2 or p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4 or p3 == p4):
            return False
        o1 = self.orient(p1,p2,p3)
        o2 = self.orient(p1,p2,p4)
        o3 = self.orient(p3,p4,p1)
        o4 = self.orient(p3,p4,p2)
        if (o1 != o2 and o3 != o4):
            return True
        # if(o1 == 0 and self.onLine(p1,p3,p2)):
        #     return True
        # if(o2 == 0 and self.onLine(p1,p4,p2)):
        #     return True
        # if(o3 == 0 and self.onLine(p3,p1,p4)):
        #     return True
        # if(o4 == 0 and self.onLine(p3,p2,p4)):
        #     return True
        if(self.onLine(p1,p3,p2) and (self.onLine(p3,p1,p4) or self.onLine(p3,p2,p4))):
            return True
        return False
    def orient(self, p1,p2,p3):
        o = (p1.y - p2.y) * (p3.x - p1.x) - (p1.x - p2.x) * (p3.y - p1.y)
        if(o==0):
            return 0
        return o/abs(o)
    # def onLine(self,p1,p2,p3):
    #     if (p2.x <= max(p2.x, p3.x) and p2.x >= min(p2.x, p3.x) and p2.y <= max(p2.y, p3.y) and p2.y >= min(p2.y, p3.y)):
    #         return True
    #
    #     return False
    def onLine(self,p1,p2,p3):
        if(p3.x==p1.x):
            slope = UPPER_DOMAIN**2
        else:
            slope = (float)(p3.y-p1.y)/(float)(p3.x-p1.x)
        if(p2.x==p1.x):
            slope1=UPPER_DOMAIN**2
        else:
            slope1 = (float)(p2.y-p1.y)/(float)(p2.x-p1.x)
        if (slope==slope1) :
            return True

        return False
    #end TODO
    def draw_num(self, num, tur):
        dots = [(-7,3),(0,3),(7,3),(-7,-3),(0,-3),(7,-3)]
        bit = "{0:b}".format(num).zfill(6)
        tur.pensize(4)
        pos = tur.pos()
        tur.up()
        idx = 0
        for i in dots:
            new_loc = (pos[0]+i[0], pos[1]+i[1])
            tur.goto(new_loc)
            if(bit[idx]=='1'):
                tur.color('black')
            else:
                tur.color('white')
            tur.down()
            tur.forward(1)
            tur.up()
            idx+=1

    def draw_nodes(self, scale_factor, show_number = False):
        bob = turtle.Turtle()
        bob.speed(0)
        bob.ht()
        bob.shape('circle')
        bob.up()
        for i in self.nodes:
            #print(i)
            bob.color(i.color)
            x = i.x*scale_factor-(0.5*UPPER_DOMAIN*scale_factor)
            y = i.y*scale_factor-(0.5*UPPER_DOMAIN*scale_factor)
            bob.goto(x,y)
            bob.stamp()
            if(type(i.name)==int and show_number):
                self.draw_num(i.name%64, bob)

    def draw_edges(self, color, scale_factor):
        bob = turtle.Turtle()
        bob.speed(0)
        bob.shape('circle')
        bob.ht()
        bob.pensize(3)
        bob.color(color)
        bob.up()
        for i in self.edges:
            x = self.get_node(i[0]).x*scale_factor-(0.5*UPPER_DOMAIN*scale_factor)
            y = self.get_node(i[0]).y*scale_factor-(0.5*UPPER_DOMAIN*scale_factor)
            bob.goto(x,y)
            bob.down()
            x = self.get_node(i[1]).x*scale_factor-(0.5*UPPER_DOMAIN*scale_factor)
            y = self.get_node(i[1]).y*scale_factor-(0.5*UPPER_DOMAIN*scale_factor)
            bob.goto(x,y)
            bob.up()

    def draw(self):
        wn = turtle.Screen()
        wn.setup(width=10*UPPER_DOMAIN, height=10*UPPER_DOMAIN)

        #JACOB: if show_number = True, there will be a binary representation of  the node name over node
        self.draw_edges("black", 10)
        #self.draw_nodes(10,show_number=True)

        self.draw_nodes(10)

        wn.exitonclick()

def find_nearest(n, nodes):
    min_dist = UPPER_DOMAIN**2
    closest = n
    closest_idx = 0
    idx = 0
    for i in nodes:
        dist = ((i.x-n.x)**2 + (i.y-n.y)**2)**(0.5)
        if(dist != 0 and dist <= min_dist):
        #if((i.x != n.x or i.y != n.y) and dist <= min_dist):
            min_dist=dist
            closest = i
            closest_idx = idx
        idx+=1
    return closest, closest_idx


def main():
    g = Graph()
    g.gen_rand_graph(100)
    #print(g.nodes)
    print(g.edges)
    g.draw()
#main()
