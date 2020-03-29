class Node:

    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

    def printPreorder(root):
        if root:
            print(root.val)
            printPreorder(root.left)
            printPreorder(root.right)