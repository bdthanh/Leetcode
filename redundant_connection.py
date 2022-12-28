from typing import List
class UnionFind:
  def __init__(self, n: int):
    self.numDisjoint = n
    self.parents = list(range(n))
    self.ranks = [0] * n
    self.sizes = [1] * n
  def find(self, node):
    parent = self.parents[node]
    childStack = []
    while parent != node:
      childStack.append(node)
      node = parent
      parent = self.parents[node]
    for child in childStack:
      self.parents[child] = parent
    return parent
  def union(self, a: int, b: int) -> bool: #modified this one to return false when detect a redundant connection
    ap = self.find(a)
    bp = self.find(b)
    
    if ap == bp:
      return False
    if self.ranks[ap] < self.ranks[bp]:
      temp = ap 
      ap = bp
      bp = temp
    # at this point ranks[ap] > ranks[bp]
    self.parents[bp] = ap
    self.sizes[ap] += self.sizes[bp]
    if self.ranks[ap] == self.ranks[bp]:
      self.ranks[ap]+=1
    return True
      
      
class Solution:
  def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    n = len(edges)
    uf = UnionFind(n)
    for pair in edges:
      if uf.union(pair[0]-1, pair[1]-1) == False:
        return pair
      
edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print(Solution().findRedundantConnection(edges))
      