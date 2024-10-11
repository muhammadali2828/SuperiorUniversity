class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
#Preorder: Visit the root first, then traverse the left subtree, followed by the right subtree.

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)
#Inorder: Traverse the left subtree, visit the root, then traverse the right subtree.
def preorder(root):
    if root:
        print(root.value)
        preorder(root.left)
        preorder(root.right)

#Postorder: Traverse the left subtree, then the right subtree, and visit the root last.
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("In-order: ")
inorder(root)
print("\nPre-orde:")
preorder(root)
print("\nPostorder: ")
postorder(root)
