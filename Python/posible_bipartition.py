from typing import List
class Solution:
  def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
    graph = [[] for i in range(n+1)]
    visited = set()
    considerList = set()
    for pair in dislikes:
      graph[pair[0]].append(pair[1])
      graph[pair[1]].append(pair[0])
      considerList.add(pair[0])
      considerList.add(pair[1])
    assignedGroup = [None for i in range(n+1)]
    canArrange = True
    
    def arrangeGroup(person: int, group: bool, canArrange) -> bool:
      if not canArrange: 
        return False
      assignedGroup[person] = group
      for dislike in graph[person]:
        if assignedGroup[dislike] == None:
          canArrange = canArrange and arrangeGroup(dislike, not assignedGroup[person], True)
        elif assignedGroup[person] == assignedGroup[dislike]:
          canArrange = False
      return canArrange
          
          
    for person in considerList:
      if assignedGroup[person] == None:
        canArrange = canArrange and arrangeGroup(person, True, True)
        if not canArrange:
          break
      
    return canArrange
        
n = 8
dislikes = [[1,2],[1,3],[4,5],[4,6],[3,5],[3,7],[5,7]]
print(Solution().possibleBipartition(n, dislikes))
        
        