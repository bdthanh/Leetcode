from typing import List, Dict
class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    def getGraph(numCourses: int, prerequisites: List[List[int]]):
      graph = [[] for i in range(numCourses)]
      for i in range(len(prerequisites)):
        graph[prerequisites[i][0]].append(prerequisites[i][1])
      return graph 
    
    def isCyclicUtil(graph: List[List[int]], visited: List[bool], processingStack, course: int) -> bool:
      #dfs modified just to check cyclic or not
      visited[course] = True
      processingStack.add(course)
      
      for prereg in graph[course]:
        if visited[prereg] == False:
          if isCyclicUtil(graph, visited, processingStack, prereg):
            return True
        elif prereg in processingStack:
          return True
        
      processingStack.remove(course)
      return False
      
    def isCyclic(graph: List[List[int]]) -> bool:
      visited = [False] * numCourses
      processingStack = set()
      
      for course in range(numCourses):
        if visited[course] == False:
          if isCyclicUtil(graph, visited, processingStack, course) == True:
            return True
      return False
    
    graph = getGraph(numCourses, prerequisites)
    return not isCyclic(graph)
  
numCourses = 5
prerequisites = [[1,4],[2,4],[3,1],[3,2]]
print(str(Solution().canFinish(numCourses, prerequisites)))
