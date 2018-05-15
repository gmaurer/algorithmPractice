from assets import graph, queue

def breadth_first_search1(graph, start, target):
    frontier = queue.Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True

    while not frontier.empty():
        current = frontier.get()
        print("Visiting %r" % current)
        if current is target:
            print("Found %r" % current)
            break
        for next in graph.neighbors(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True


def breadth_first_search2(graph, start):
    frontier = queue.Queue()
    frontier.put(start)
    came_from = dict()
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()
        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current

    return came_from

def preorder_binary_breadth_first_search(root):
    if root:
        print(root.value)
        preorder_binary_breadth_first_search(root.left)
        preorder_binary_breadth_first_search(root.right)
