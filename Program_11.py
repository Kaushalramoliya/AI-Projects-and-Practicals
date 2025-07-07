'''  
@author: 22000409 Kaushal Ramoliya  
@description: 10. - Write a program in Python for A* Search
'''  
from queue import PriorityQueue

class GraphAlgorithm:
    def __init__(self, graph):
        self.graph = graph
        self.visited = [] 

    def astar(self,start,goal):
        pq=[[0,0,0,start]] # Priority queue: (f, h, g, node, path)
        self.visited=[]
        while pq:
            f,h,g,cnode=pq.pop(0)
            self.visited.append([f,h,g,cnode])
            for neigh, wt in self.graph[cnode[-1]].items():
                g1=g+wt[0]
                f1=g1+wt[1]
                path=cnode+neigh
                pq.append([f1,wt[1],g1,path])
                pq=sorted(pq)
    
        res_visited=[]
        for x in self.visited:
            if x[3].endswith(goal):
                res_visited.append(x)
        return sorted(res_visited)

graph = {
     'A': {'B': [3,8], 'C': [2,9]},
     'B': {'D': [3,7], 'E': [4,6]},
     'C': {'F': [5,4]},
     'D': {'G': [6,0]},
     'E': {'G': [9,0]},
     'F': {'G': [6,0]},
     'G': {}
}
start = 'A'
goal = 'G'

print("Following is the A* Algorithm.")
astar_SearchAlgorithm = GraphAlgorithm(graph)
result=(astar_SearchAlgorithm.astar(start, goal))
print("Goal reached using Path-->", result[0][-1], "and with cost of: ", result[0][-2])