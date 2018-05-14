from assets import graph
from assets import queue

def breadth_first_search(graph,start,target):
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
