'''  
@author: 22000409 Kaushal Ramoliya  
@description: 7. - Write a program in Python to implement Depth First Search.
'''  
class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.visited = []
        self.stack = []
    
    def dfs(self, start_node):
        self.stack.insert(0, start_node)
        
        while self.stack:
            node = self.stack.pop(0)
            if node not in self.visited:
                self.visited.append(node)
                for child in self.graph[node]:
                    if child not in self.visited:
                        self.stack.insert(0, child)
        
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

# Driver code
print("Following is the Depth First Search")
graph.dfs('A')
