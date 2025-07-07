'''  
@author: 22000409 Kaushal Ramoliya  
@description: 8. - Implement BFS and DFS on following graph.
'''  
from collections import deque

class GraphSearch:
    def __init__(self, graph):
        self.graph = graph

    def My_BLS(self, start, goal, limit):
        queue = deque([(start, 0)])  # Use deque for queue functionality
        while queue:
            node, depth = queue.popleft()  # Pop from the left for BFS
            if node == goal:
                return True, goal, depth
            if depth < limit:
                for n in self.graph.get(node, []):
                    queue.append((n, depth + 1))
        return False, goal, -1  # Fixed the return statement

    def My_DLS(self, start, goal, limit):
        stack = [(start, 0)]
        while stack:
            node, depth = stack.pop()
            if node == goal:
                return True, goal, depth
            if depth < limit:
                for n in self.graph.get(node, []):
                    stack.append((n, depth + 1))
        return False, goal, -1  # Fixed the return statement

graph_data = {
    'Jodhpur': ['Barmer', 'Sawai Madhopur'],
    'Barmer': ['Mount Abu', 'Udaipur'],
    'Sawai Madhopur': ['Kota', 'Shivpuri'],
    'Mount Abu': ['Mehsana'],
    'Udaipur': ['Himatnagar'],
    'Kota': ['Ratlam'],
    'Shivpuri': ['Ratlam'],
    'Mehsana': ['Ahmedabad'],
    'Himatnagar': ['Ahmedabad'],
    'Ratlam': ['Vadodara'],
    'Ahmedabad': ['Rajkot', 'Vadodara'],
    'Rajkot': ['Vadodara'],
    'Vadodara': []
}

search = GraphSearch(graph_data)
limit = 8

print("using BFS")
b, g, d = search.My_BLS('Jodhpur', 'Vadodara', limit)
if b:
    print("Goal", g, "found at level", d)
else:
    print("Goal", g, "not found within limit", limit)

print("using DFS")
b, g, d = search.My_DLS('Jodhpur', 'Vadodara', limit)
if b:
    print("Goal", g, "found at level", d)
else:
    print("Goal", g, "not found within limit", limit)
