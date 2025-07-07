'''  
@author: 22000409 Kaushal Ramoliya  
@description: 17. - implement A* search on the following graph.
'''  
from queue import PriorityQueue

class GraphAlgorithm:
    def __init__(self, graph):
        self.graph = graph
        self.visited = []

    def astar(self, start, goal):
        # pq entries are [f = g+h, h, g, path_list]
        pq = [[0, 0, 0, [start]]]
        self.visited = []

        while pq:
            f, h, g, path = pq.pop(0)
            node = path[-1]
            self.visited.append([f, h, g, path])

            if node == goal:
                break

            for neigh, (cost, h_neigh) in self.graph[node].items():
                g2 = g + cost
                f2 = g2 + h_neigh
                new_path = path + [neigh]
                pq.append([f2, h_neigh, g2, new_path])

            pq.sort(key=lambda x: x[0])

        # filter only those that actually reached the goal
        finals = [v for v in self.visited if v[3][-1] == goal]
        return sorted(finals, key=lambda x: x[0])



graph = {
    'Vadodara': {
        'Godhra':       [3, 9],
        'Kevadia':      [3,10],
        'ChhotaUdepur': [4,12],
    },
    'Godhra': {
        'Vadodara': [3, 0],
        'Kevadia':  [9,10],
        'Dahod':    [6, 6],
    },
    'Kevadia': {
        'Vadodara': [3, 0],
        'Godhra':   [9, 9],
        'Thandla':  [2, 5],
    },
    'ChhotaUdepur': {
        'Vadodara': [4, 0],
        'Khargone': [9, 9],
    },
    'Khargone': {
        'ChhotaUdepur': [9,12],
        'Barwaha':      [9, 8],
    },
    'Barwaha': {
        'Khargone': [9, 9],
        'Indore':   [8, 0],
    },
    'Dahod': {
        'Godhra': [6, 9],
        'Ujjain': [5, 4],
        'Thandla':[3, 5],
    },
    'Ujjain': {
        'Dahod':   [5, 6],
        'Indore':  [4, 0],
    },
    'Thandla': {
        'Kevadia': [2,10],
        'Dahod':   [3, 6],
        'Dhar':    [3, 3],
    },
    'Dhar': {
        'Thandla': [3, 5],
        'Indore':  [2, 0],
    },
    'Indore': {
        'Ujjain': [4, 4],
        'Barwaha':[8, 8],
        'Dhar':   [2, 3],
    }
}

start = 'Vadodara'
goal  = 'Indore'

astar = GraphAlgorithm(graph)
results = astar.astar(start, goal)

if results:
    best = results[0]
    path_list = best[3]
    cost = best[2]
    print("Best path:", " -> ".join(path_list))
    print("Total cost:", cost)
else:
    print("No path found!")
