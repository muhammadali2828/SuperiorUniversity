class Node:
    def __init__(self,value):
        self.value = value
        self.next = []  

def Dfs_stack(root):
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.value)
        for i in node.next: 
            stack.append(i)

root = Node(1)
root.next = [Node(2), Node(3)]
root.next[0].next = [Node(4), Node(5)]

Dfs_stack(root)
