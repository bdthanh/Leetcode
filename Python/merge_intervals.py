from typing import List 
from operator import itemgetter
class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals = sorted(intervals, key=itemgetter(0))
    result = []
    i=0
    while i < len(intervals):
      temp_interval = intervals[i]
      
      while i+1 < len(intervals) and temp_interval[0] <= intervals[i+1][0] <= temp_interval[1]:
        temp_interval[1] = max(temp_interval[1], intervals[i+1][1])
        i+=1
      result.append(temp_interval)
      i+=1
    return result
      
  
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(Solution().merge(intervals))