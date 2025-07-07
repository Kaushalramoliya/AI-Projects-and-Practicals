'''  
@author: 22000409 Kaushal Ramoliya  
@description: 6. - Write a python program to implement Breadth First Search and Depth First Search algorithm 
on following graph. Consider start node as A. 
'''  
class Graph:
    def __init__(self, graph):
        self.graph = graph

    def bfs(self, start_node):
        visited = []
        queue = []

        queue.append(start_node)
        visited.append(start_node)

        while queue:
            node = queue.pop(0)
            for child in self.graph[node]:
                if child not in visited:
                    queue.append(child)
                    visited.append(child)

        print("BFS Traversal:", visited)

    def dfs(self, start_node):
        visited = []
        stack = []

        stack.insert(0, start_node)

        while stack:
            node = stack.pop(0)
            if node not in visited:
                visited.append(node)
                for child in reversed(self.graph[node]):  
                    if child not in visited:
                        stack.insert(0, child)

        print("DFS Traversal:", visited)

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

# Run both traversals
print("Following is the Breadth First Search")
graph.bfs('A')

print("\nFollowing is the Depth First Search")
graph.dfs('A')
