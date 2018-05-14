from assets import graph,square_grid
from algorithms import bfs

testGraph = graph.SimpleGraph()
testGraph.edges = {
'a':['b'],
'b':['a','c','d'],
'c':['a'],
'd':['e','a'],
'e':['b']
}

bfs.breadth_first_search(testGraph,'c',None)


g = square_grid.SquareGrid(6,8)
g.walls = [(4,2), (4,3), (5,2), (5,3), (5,4), (1,5), (2,5), (1,4), (2,4)]
