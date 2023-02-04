# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:        
    def invert(subRoot: TreeNode):
      if subRoot == None:
        return
      subRoot.left, subRoot.right = subRoot.right, subRoot.left
      invert(subRoot.left)
      invert(subRoot.right)

    invert(root)
    return root