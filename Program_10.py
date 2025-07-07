'''  
@author: 22000409 Kaushal Ramoliya  
@description: 10. - Write a python program to implement Uniform Cost Search with cumulative cost.
'''  
from queue import PriorityQueue

class UCS:
    def __init__(self, graph_data):
        self.graph = graph_data

    def ucsAlgo(self, start, goal):
        queue = PriorityQueue()
        queue.put((0, start, [start])) 
        visited = set()
        
        while queue:
            cost, node, path = queue.get()
            
            if node in visited:
                continue
            
            visited.add(node)
            
            if node == goal:
                print("Visited nodes:", path)
                print("Total cost:", cost)
                return
            
            for child, weight in self.graph[node].items():
                if child not in visited:
                    queue.put((cost + weight, child, path + [child]))
        
        print("Goal not reachable")

# Graph representation
graph_data = {
    'S': {'A': 1, 'G': 12},
    'A': {'B': 3, 'C': 1},
    'B': {'D': 3},
    'C': {'D': 1, 'G': 2},
    'D': {'G': 3},
    'G': {}
}

ucs = UCS(graph_data)
print("Following is the Uniform Cost Search with cumulative cost:")
ucs.ucsAlgo('S', 'G')