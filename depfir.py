class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def prtLevelOrder(root):
        h = height(root)
        for i in range(1, h+1):
            prtLevelOrder(root, i)

    def prtLevel(root , level):
        if root is None:
            return
        if level == 1:
            print (root.data)
        elif level > 1 :
            prtLevelOrder(root.left , level-1)
            prtLevelOrder(root.right , level-1)