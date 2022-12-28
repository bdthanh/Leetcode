from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    def traversal(root: Optional[TreeNode]):
      if root == None:
        return
      traversal(root.left)
      inorder.append(root.val)
      traversal(root.right)
    inorder = []
    traversal(root)
    return inorder