'''  
@author: 22000409 Kaushal Ramoliya  
@description: 5. - Write a program in Python for Breadth First Search.
'''  
class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.visited = []
        self.queue = []
    
    def bfs(self, start_node):
        self.queue.append(start_node)
        self.visited.append(start_node)
        
        while self.queue:
            node = self.queue.pop(0)
            for child in self.graph[node]:
                if child not in self.visited:
                    self.queue.append(child)
                    self.visited.append(child)
        
        print("Visited:", self.visited)

# Graph definition
graph_data = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['H'],
    'F': ['H'],
    'G': ['H'],
    'H': []
}

# Creating Graph object
graph = Graph(graph_data)
print("Following is the Breadth First Search")
graph.bfs('A')
