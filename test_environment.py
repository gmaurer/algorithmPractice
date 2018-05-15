from assets import graph, square_grid, node
from algorithms import bfs
import pprint

testGraph = graph.SimpleGraph()
testGraph.helper_add_node('abcde')
testGraph.helper_add_neighbors('a','b')
testGraph.helper_add_neighbors('b','acd')
testGraph.helper_add_neighbors('c','a')
testGraph.helper_add_neighbors('d','ea')
testGraph.helper_add_neighbors('e','b')

bfs.breadth_first_search1(testGraph,'a',None)


g = square_grid.SquareGrid(6,8)
g.walls = [(4,2), (4,3), (5,2), (5,3)]#, (5,4), (1,5), (2,5), (1,4), (2,4)]
#pprint.pprint(bfs.breadth_first_search2(g, (2,2)))

root = node.Node(1)
root.create_random_node(3)
#root.add_node(root,2)
#root.add_node(root.left,3)
#root.add_node(root,4)
#root.add_node(root.left,7)
bfs.preorder_binary_breadth_first_search(root)
