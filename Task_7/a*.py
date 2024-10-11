def astar(grid, start, goal):
    x, y = start
    gx, gy = goal

    open_list = [start]  
    closed_list = []    
    came_from = {}

    g_cost = {start: 0}
    h_cost = {start: abs(gx - x) + abs(gy - y)}

    while open_list:
        
        current = open_list[0]
        for pos in open_list:
            if g_cost[pos] + h_cost[pos] < g_cost[current] + h_cost[current]:
                current = pos

        if current == goal:
            
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1] 

        open_list.remove(current)
        closed_list.append(current)

        x, y = current

        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        for neighbor in neighbors:
            nx, ny = neighbor
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                if neighbor in closed_list:
                    continue

                new_g_cost = g_cost[current] + 1

                if neighbor not in open_list or new_g_cost < g_cost.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_cost[neighbor] = new_g_cost
                    h_cost[neighbor] = abs(gx - nx) + abs(gy - ny)
                    if neighbor not in open_list:
                        open_list.append(neighbor)

    return None  # No path found
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)   
goal = (4, 4)   

path = astar(grid, start, goal)

if path:
    print("Path fouund:", path)
else:
    print("No path found")
