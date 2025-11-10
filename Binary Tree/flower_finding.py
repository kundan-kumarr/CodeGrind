"""


Input: root [inventory], target [string input]
Output: Boolean

M:
Recursive
Node Comparison

P:
1. Empty input [ie nonexsistant tree]
    return False
2. Make target lowercase()
    Every single node, make it lowercase()
3. Recurisve:
    if node.val.lowercase() == target.lowercase():
            return True
    recurive call left 
    recurive call right 
        

"""
from collections import deque 
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

def find_flower(inventory, name):
    if not inventory:
        return False
    if inventory.val.lower() == name.lower():
        return True
    
    elif name < inventory.val:
        left_check = find_flower(inventory.left, name)
        return left_check
    else:
        return find_flower(inventory.right, name)
   

# using build_tree() function at top of page
values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]

garden = build_tree(values)

print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower")) 

