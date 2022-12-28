from typing import Optional
# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
    # the case when p has right node 
    if p.right != None:
      p = p.right
      while p.left != None:
        p = p.left
      return p
    ans = TreeNode(0)
    mi = 2**31-1
    def findP(root: TreeNode, mi: int, ans: TreeNode) -> TreeNode:
      if root.val == p.val:
        return ans
      elif root.val > p.val: 
        if root.val < mi:
          ans = root
          mi = ans.val
        return findP(root.left, mi, ans)
      else: #root.val < p:
        return findP(root.right, mi, ans)
    ans = findP(root, mi, ans)
    return ans

root = x = TreeNode(2)
p = x.left = TreeNode(1)
x.right = TreeNode(3)
print(Solution().inorderSuccessor(root, p).val)