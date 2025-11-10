'''
Given the root of a binary tree where each node represents the number of splits in a leaf of a Monstera plant, return the number of Monstera leaves 🍃 that have an odd number of splits.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

Note: The term leaf in this problem refers to the plant leaf 🍃 of a Monstera plant, not the type of node leaf nodes which are nodes with no children.

understand:
input: array of vals
output: integer (a count)

edgecase:
empty inputs: return 0
invalid inputs: question for the interviewer (neagtive inputs?)  (we just count all the odd -ve inputs)
- the array is not sorted

We know:
- that the tree is connected:
hypothesis:
- we should traverse the tree and see if each node is even or odd, if it is odd increment it by one. 

Plan:
edgecase handling
- Create a variable called count
- loop throuh the tree
    - access each value,
        - if val % 2 != 0
            - count++
return count


'''

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
          
def count_odd_splits(root):
    if root is None:
        return 0

    node = [root]
    count = 0 
    
    if root.val % 2 != 0:
        count += 1
    count += count_odd_splits(root.left)
    count += count_odd_splits(root.right)

    return count
   
'''
    # while node:
    #     check_node = node.pop()
    #     if check_node.val % 2 !=0:
    #         count +=1
    #     if check_node.right:
    #         node.append(check_node.right)
    #     if check_node.left:
    #         node.append(check_node.left)
    # return count 
    '''
        
values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

print(count_odd_splits(monstera))
print(count_odd_splits(None))
