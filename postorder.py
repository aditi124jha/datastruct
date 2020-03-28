class Node:
def __init__(self,key):
self.left = None
self.right = None
self.val = key

def printPostorder(root):
if root:
printPostorder(root.left)
printPostorder(root.right)
print(root.val)