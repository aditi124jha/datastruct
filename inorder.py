class Node:
    
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

    def printInorder(root):
        if root:
            printInorder(root.left)
            print(root.val)
            printInorder(root.right)