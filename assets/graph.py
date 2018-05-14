

class SimpleGraph:
    def __init__(self):
        self.edges = {}

    def neighbors(self, id):
        return self.edges[id]



testGraph = SimpleGraph()
testGraph.edges = {
'a':['b'],
'b':['a','c','d'],
'c':['a'],
'd':['e','a'],
'e':['b']
}
