

class SimpleGraph:
    def __init__(self):
        self.edges = dict()

    def neighbors(self, id):
        return self.edges[id]

    def add_neighbor(self,a,b):
        if b not in self.edges[a]:
            self.edges[a].append(b)

    def add_node(self,a):
        if a not in self.edges.keys():
            self.edges[a] = list()

    def helper_add_neighbors(self,a,b):
        for x in b:
            self.add_neighbor(a,x)

    def helper_add_node(self,a):
        for x in a:
            self.add_node(x)



testGraph = SimpleGraph()
for x in 'abcde':
    testGraph.add_node(x)

testGraph.helper_add_neighbors('a','b')
testGraph.helper_add_neighbors('b','acd')
testGraph.helper_add_neighbors('c','a')
testGraph.helper_add_neighbors('d','ea')
testGraph.helper_add_neighbors('e','b')
