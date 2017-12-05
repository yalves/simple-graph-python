import collections
from implementation import *

exercise_graph = SimpleGraph()
exercise_graph.edges = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['E', 'D'],
    'D': ['G'],
    'E': ['G', 'D', 'F'],
    'F': [],
    'G': []
}

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
    
    return came_from, cost_so_far

#a_star_search(exercise_graph, 'A', 'G')

# start, goal = (1, 4), (7, 8)
# came_from, cost_so_far = a_star_search(diagram4, start, goal)
# # draw_grid(diagram4, width=3, point_to=came_from, start=start, goal=goal)
# # print()
# draw_grid(diagram4, width=3, number=cost_so_far, start=start, goal=goal)
# print()

g = SquareGrid(30, 15)
g.neighbors((21,12))
g.neighbors((4,5))
g.walls = DIAGRAM1_WALLS # long list, [(21, 0), (21, 2), ...]
draw_grid(g)