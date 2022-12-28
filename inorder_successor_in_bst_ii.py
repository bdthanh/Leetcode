
# Definition for a Node.
class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.parent = None


class Solution:
  def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
    if node.right != None:
      node = node.right
      while node.left != None:
        node = node.left
      return node
    
    if node.parent == None:
      return None
    print(node.parent.left.val,node.val)
    while node.parent != None and node.parent.left.val != node.val:
      node = node.parent
    return node.parent

root = x = Node(2)
x.left = Node(1)
x.left.parent = root
x.right = Node(3)
x.right.parent = root
print(Solution().inorderSuccessor(x.left).val)