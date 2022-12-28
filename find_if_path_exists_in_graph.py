from typing import List, Set
class Solution:
  def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    def getGraph():
      graph = [set() for _ in range(n)]
      for pair in edges:
        graph[pair[0]].add(pair[1])
        graph[pair[1]].add(pair[0])
      return graph
    
    visited = set()
    stack = [source]
    def bfs(graph: List[Set[int]], source: int, destination: int) -> bool:
      if source == destination:
        return True
      if len(visited) == n:
        return False
      curNode = stack.pop()
      visited.add(curNode)
      for node in graph[curNode]:
        if not node in visited:
          stack.append(node)
      if len(stack) == 0:
        return False
      return bfs(graph, stack[-1], destination)
    
    graph = getGraph()
    return bfs(graph, source, destination)
  
n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5
print(Solution().validPath(n, edges, source, destination))