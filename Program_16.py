'''  
@author: 22000409 Kaushal Ramoliya  
@description: 16. - Write a program to implement A* search on the following graph. 
'''  
from queue import PriorityQueue
from geopy.distance import geodesic

raw_graph = {
    'START': {'Jammu': [32.7266,74.8570,1600]},
    'Jammu': {'Amritsar': [31.6339, 74.8722,1400], 'Delhi': [28.7040,77.1024,1300]},
    'Amritsar': {'Sri-Gangaganar': [29.9094,73.8800,1340], 'Jodhpur': [26.2389,73.0243,1230]},
    'Delhi': {'Jaipur': [26.9124, 75.7873,1000], 'Gwalior': [26.2124, 78.1772,1100]},
    'Sri-Gangaganar': {'Udaipur': [24.5854, 73.7125,400]},
    'Jodhpur': {'Himmatnagar': [23.5969, 72.9630,300]},
    'Jaipur': {'Kota': [25.2138, 75.8648,300]},
    'Gwalior': {'Ratlam': [23.3315,75.0367,250]},
    'Udaipur': {'Vadodara': [22.3072,73.1812,0]},
    'Himmatnagar': {'Vadodara': [22.3072,73.1812,0]},
    'Kota': {'Vadodara': [22.3072,73.1812,0]},
    'Ratlam': {'Vadodara': [22.3072,73.1812,0]},
}

def build_graph(raw_graph):
    graph = {}
    coords = {} 

    for node in raw_graph:
        if node not in coords and node != 'START':
            continue
        graph[node] = {}
        for neighbor, (lat, lon, heuristic) in raw_graph[node].items():
            coords[neighbor] = (lat, lon)
            if node == 'START':
                coords['START'] = (0, 0)  
                distance = 0
            else:
                distance = geodesic(coords[node], (lat, lon)).km
            graph[node][neighbor] = [distance, heuristic]
    return graph

def a_star_search(graph, start, goal):
    pq = PriorityQueue()  # (f, h, g, node, path)
    pq.put((0, 0, 0, start, [start]))
    visited = {}

    while not pq.empty():
        f, h, g, current, path = pq.get()

        if current in visited and visited[current] <= g:
            continue

        visited[current] = g

        if current == goal:
            return path, round(g, 2)

        for neighbor, (cost, heuristic) in graph.get(current, {}).items():
            new_g = g + cost
            new_f = new_g + heuristic
            pq.put((new_f, heuristic, new_g, neighbor, path + [neighbor]))

    return None, float('inf')

graph = build_graph(raw_graph)
start = 'Jammu'
goal = 'Vadodara'

path, cost = a_star_search(graph, start, goal)

print("Optimal Path:", path)
print("Total Distance (km):", cost)
