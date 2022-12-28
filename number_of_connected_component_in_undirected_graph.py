from typing import List

# inspired by Prof Halim's UFDS implementation: canvas.nus.edu.sg/courses/25203/pages/dear-students-welcome?module_item_id=25446
class Union_Find:
  def __init__(self, n: int):
    self.numConnectedComponent = n #when initializing, all components are seraprated so number of disjoint = n 
    self.ranks = [0] * n
    self.parents = [x for x in range(n)] 
    self.sizes = [1] * n #when initializing, size of all disjoint components are 1 
  
  def find(self, component: int) -> int: # return the parent/root of that component
    parent = self.parents[component]
    childrenStack = []
    while parent != component:
      childrenStack.append(component)
      component = self.parents[component]
      parent = self.parents[component]
    for child in childrenStack:
      self.parents[child] = parent
    return parent
  
  def union(self, component1: int, component2: int) -> int: # join 2 components
    parent1 = self.find(component1)
    parent2 = self.find(component2)
    
    if parent1 == parent2:
      return 
    
    if self.ranks[parent1] < self.ranks[parent2]:
      self.parents[parent1] = parent2
      self.sizes[parent2] += self.sizes[parent1]
    elif self.ranks[parent2] < self.ranks[parent1]:
      self.parents[parent2] = parent1
      self.sizes[parent1] += self.sizes[parent2]
    else:
      self.parents[parent1] = parent2
      self.sizes[parent2] += self.sizes[parent1]
      self.ranks[parent2] += 1
    
    self.numConnectedComponent -= 1
    
class Solution:
  def countComponents(self, n: int, edges: List[List[int]]) -> int:
    uf = Union_Find(n)
    for edge in edges:
      uf.union(edge[0], edge[1])
    return uf.numConnectedComponent

n = 5
edges = [[0,1],[1,2],[2,3],[3,4]]
print(Solution().countComponents(n, edges))