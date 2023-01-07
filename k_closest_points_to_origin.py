import math
import heapq
from typing import List
class Solution:
  def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]: #O(klogn)
    distances = []
    for i in range(len(points)):
      dist = math.sqrt(points[i][0]*points[i][0] + points[i][1]*points[i][1])
      distances.append([dist, i])
    heapq.heapify(distances)
    ans = []
    for i in range(k):
      ans.append(points[heapq.heappop(distances)[1]])
    return ans
  
class Solution:
  def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    def calDist(id: int):
      return math.sqrt(points[i][0]*points[i][0] + points[i][1]*points[i][1])
    
    


  
points = [[1,3],[-2,2]]
k = 1
print(Solution().kClosest(points, k))
      
    
      