'''  
@author: 22000409 Kaushal Ramoliya  
@description: 13. - Write a program to implement UCS on following graph. 
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

graph_data = { 
    'A': {'B': 1, 'C': 2}, 
    'B': {'D': 3, 'E': 4}, 
    'C': {'F': 5}, 
    'D': {'G': 6}, 
    'E': {'G': 7}, 
    'F': {'G': 8}, 
    'G': {} 
} 

ucs = UCS(graph_data)
print("Following is the Uniform Cost Search with cumulative cost:")
ucs.ucsAlgo('A', 'G')