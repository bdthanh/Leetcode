from typing import List, Dict, Set
class Solution:
  def validTree(self, n: int, edges: List[List[int]]) -> bool:
    def getGraph():
      graph = [set() for i in range(n)]
      for pair in edges:
        graph[pair[0]].add(pair[1])
        graph[pair[1]].add(pair[0])
      return graph
    
    def isValidUsingModifiedDfsUtil(graph: List[List[int]], visited: Set[int], node: int) -> bool:
      visited.add(node)
      for adjacent in graph[node]:
        if adjacent in visited:
          return False
        graph[adjacent].remove(node)
        if not isValidUsingModifiedDfsUtil(graph, visited, adjacent):
          return False
      return True
        
    
    def isValidUsingModifiedDfs(graph: List[List[int]], visited: Set[int]) -> bool:
      startNode = 0
      return isValidUsingModifiedDfsUtil(graph, visited, startNode) and len(visited) == n
    
    graph = getGraph()
    visited = set()
    return isValidUsingModifiedDfs(graph, visited)
    
    
    
n = 4
edges = [[0,1],[2,3]]
print(str(Solution().validTree(n, edges)))