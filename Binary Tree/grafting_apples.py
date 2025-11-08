"""
You are grafting different varieties of apple onto the same root tree can produce many different varieties of apples! Given the following TreeNode class, create the binary tree depicted below. The text representing each node should should be used as the value.

The root, or topmost node in the tree TreeNode("Trunk") has been provided for you.
"""
from collections import deque 
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
        
# Leaf nodes

fuji = TreeNode("Fuji")
opal = TreeNode("Opal")
crab = TreeNode("Crab")
gala = TreeNode("Gala")

# Intermediate 

macintosh = TreeNode("Mcintosh",fuji, opal)
granny_smith = TreeNode("Granny Smit",crab, gala)

root = TreeNode("Trunk")
root.left = macintosh
root.right = granny_smith

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)
    
print_tree(root)

