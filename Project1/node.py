

class Node:

    def __init__(self, name= "",x=0,y=0,color=None,domain=[]):
        self.name = name
        self.x = x
        self.y = y
        self.color = color
        self.domain = domain

    def __str__(self):
        string = 'node:' +str(self.name)+ '; x: ' +str(self.x)+'; y: ' +str(self.y)+'; color: ' +str(self.color)+'; domain: ' +str(self.domain)
        return string
    def set_nodes(self, x, y):
        self.x = x
        self.y = y
