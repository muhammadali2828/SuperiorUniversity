tree = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F','G'],
    'D': [],
    'E': [],
    'F': [],
    'G': [],
}

def bfs_no_queue(start):
    visited = []
    remaining = [start]

    while remaining:
        node = remaining[0]
        remaining = remaining[1:]  
        if node not in visited:
            visited.append(node)
            remaining += tree [node]  
    return visited

print(bfs_no_queue('A'))
