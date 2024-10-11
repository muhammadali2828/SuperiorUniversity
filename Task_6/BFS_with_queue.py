class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

def bfs_with_queu(start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(node.neighbors)  
    return [node.value for node in visited]

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F= Node('F')
G= Node('G')

A.neighbors = [B,C]
B.neighbors = [D,E]
C.neighbors = [F,G]

print(bfs_with_queu(A))
