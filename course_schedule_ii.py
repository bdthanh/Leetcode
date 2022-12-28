from typing import List
class Solution:
  def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[List[int]]:
    def getGraph():
      graph = [[] for i in range(numCourses)]
      for pair in prerequisites:
        graph[pair[0]].append(pair[1])
      return graph
    
    def topoSortUtilAndCheckCyclic(graph: List[List[int]], topoSequence: List[int], visited: List[bool], isInProcessingStack: List[bool], course: int) -> bool:
      visited[course] = True
      isInProcessingStack[course] = True
      
      for prereg in graph[course]:
        if visited[prereg] == False:
          if topoSortUtilAndCheckCyclic(graph, topoSequence, visited, isInProcessingStack, prereg) == True:
            return True
        elif isInProcessingStack[prereg] == True:
          return True
      topoSequence.append(course)
      isInProcessingStack[course] = False
      return False 
    
    def topoSort(graph: List[List[int]]) -> List[int]:
      topoSequence = []
      visited = [False] * numCourses
      isInProcessingStack = [False] * numCourses
      for course in range(numCourses):
        if visited[course] == False:
          if topoSortUtilAndCheckCyclic(graph, topoSequence, visited, isInProcessingStack, course) == True: 
            return []
      return topoSequence
    
    graph = getGraph()
    return topoSort(graph) 
  
numCourses = 2
prerequisites = [[1,0]]
print(Solution().findOrder(numCourses, prerequisites))
        