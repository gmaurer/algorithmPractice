from assets import graph, square_grid, node
from structures import bfs, dfs, bst, singlely_linked_list, doubly_linked_list
from sortings import bubble, insertion
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
root.create_random_node(2)
#root.add_node(root,2)
#root.add_node(root.left,3)
#root.add_node(root,4)
#root.add_node(root.left,7)
print("pre: ")
dfs.preorder_binary_depth_first_search(root)
print()
print("post: ")
dfs.postorder_binary_depth_first_search(root)
print()
print("in: ")
dfs.inorder_binary_depth_first_search(root)

print()
root1 = bst.binary_search_tree("52351")
dfs.inorder_binary_depth_first_search(root1)
print()


print("Linked List")
lList = singlely_linked_list.LinkedList()
lList.append(4)
lList.append(1)
lList.append(7)
lList.reverse_list1()
lList.print_list()
lList.append(10)
lList.push_to_front(2)
print("reverse")
lList.reverse_list1()
lList.insert_after(lList.head.next.next,3)  #this needs to be changed
lList.print_list()

print("Doubly Linked List")
dLList = doubly_linked_list.LinkedList()
dLList.append_rear(4)
dLList.append_rear(1)
dLList.append_rear(7)
dLList.append_rear(10)
dLList.print_list()

print(bubble.bubble_sort([5,3,2,4,2]))
print(insertion.insertion_sort([4,2,3,4,1]))
