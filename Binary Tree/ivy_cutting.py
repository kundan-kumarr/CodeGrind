"""
 Ivy Cutting
You have a trailing ivy plant represented by a binary tree. You want to take a cutting to start a new plant using the rightmost vine in the plant. Given the root of the plant, return a list with the value of each node in the path from the root node to the rightmost leaf node. If there is no right child, return only the root node value (the rightmost path in this case is just the root node).

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
    if not root:
        return []
    right_path =[root.val]
    if root.right:
        right_path += right_vine(root.right)
    
    return right_path

ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))
        
  
"""
If you implemented right_vine() iteratively in the previous problem, implement it recursively. If you implemented it recursively, implement it iteratively.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
"""

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
    if not root:
        return []
    
    right_path =[]
    while root:
        right_path.append(root.val)
        root = root.right
        
    return right_path

ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))
        
  
