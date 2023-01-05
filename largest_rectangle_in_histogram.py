from typing import List
class Solution1: #Time complexity: O(nlogn) - Worst case: O(n^2) | Space complexity: O(1)
  def largestRectangleArea(self, heights: List[int]) -> int:
    def findLargest(maxSoFar: int, beg: int, end: int) -> int:
      minSoFar = heights[beg]
      minId = beg
      for i in range(beg,end+1):
        if minSoFar > heights[i]:
          minSoFar = heights[i]
          minId = i
      maxSoFar = max(maxSoFar, minSoFar*(end-beg+1))
      if beg == end: 
        return maxSoFar
      if minId != beg:
        maxSoFar = findLargest(maxSoFar, beg, minId-1)
      if minId != end:
        maxSoFar = findLargest(maxSoFar, minId+1, end)    
      return maxSoFar
         
    return findLargest(-1, 0, len(heights)-1)
  
class Solution2: #Time complexity: O(n) | Space complexity: O(n)
  def largestRectangleArea(self, heights: List[int]) -> int:
    maxSoFar = -1
    stack = []
    i=0
    while i < len(heights):
      cur = [heights[i], i]
      while len(stack) != 0 and stack[-1][0] > heights[i]:
        pop = stack.pop()
        maxSoFar = max(maxSoFar, (i - pop[1]) * pop[0])
        cur[1] = pop[1]
      stack.append(cur)
      i+=1
    while len(stack) != 0:
      pop = stack.pop()
      maxSoFar = max(maxSoFar, (i - pop[1]) * pop[0])
    return maxSoFar
    
      

heights = [2,1,5,6,2,3]
print(Solution().largestRectangleArea(heights))