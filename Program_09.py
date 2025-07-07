'''  
@author: 22000409 Kaushal Ramoliya  
@description: 9. - Write a program in Python for Best First Search
'''  
from queue import PriorityQueue

class Best:
    def __init__(self, graph):
        self.graph_data = graph
        self.visited = [] 

    def bestf(self, node, goal):
        self.visited.append(node)
        while True:
            tn = node
            if tn == goal:
                break
            queue = PriorityQueue()
            for neighbour, weight in self.graph_data[tn].items():
                queue.put([weight, neighbour])
                
            tw, tn = queue.queue[0]
            self.visited.append(tn)
            node = tn
        print("Visited:", self.visited)

# Graph definition
graph = {
'A':{'B':12, 'C':14}, #heuristic value A to H is 13, B to H is 12, C to H is 4
'B':{'D':11, 'E':10},
'C':{'F':6, 'G':7},
'D':{'H':0},
'E':{'H':0},
'F':{'H':0},
'G':{'H':0}
}   

# Creating Graph object
graph = Best(graph)

# Driver code
print("Following is the Best First Search")
graph.bestf('A', 'H')