'''  
@author: 22000409 Kaushal Ramoliya  
@description: 12. - Write a program to implement Depth Limited Search and Iterative Deepening Search on following graph/tree. 
'''  
class SearchAlgorithms:
    def __init__(self, graph):
        self.graph = graph

    def dls(self, start, goal, limit):
        stack = [(start, 0)]
        while stack:
            node, depth = stack.pop()
            if node == goal:
                return True, goal, depth
            if depth < limit:
                for child in self.graph[node]:
                    stack.insert(0, (child, depth + 1))
        return False, goal, -1

    def iddfs(self, start, goal, max_limit):
        for depth in range(max_limit + 1):
            found, g, d = self.dls(start, goal, depth)
            if found:
                print(f"Goal {g} found at level {d} using IDDFS (limit = {depth})")
                return
            else:
                print(f"Goal {goal} not found at level {depth}")
        print(f"Goal {goal} not found within max depth limit {max_limit}")


# Graph definition
graph_data = {
    '6': ['4', '8'],
    '4': ['3', '5'],
    '8': ['9'],
    '3': ['10'],
    '5': ['11'],
    '9': ['12'],
    '10': [],
    '11': [],
    '12': []
}

search = SearchAlgorithms(graph_data)

print("using DLS")
limit = 3
found, goal, depth = search.dls('6', '10', limit)
if found:
    print("Goal", goal, "found at level", depth, "using DLS")
else:
    print("Goal", goal, "not found within the depth limit using DLS")

print("\nusing IDDFS")
search.iddfs('6', '10', limit)
