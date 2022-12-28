from collections import deque
from typing import List
class Solution:
  def trap(self, height: List[int]) -> int:
    dq = deque([]) # the first/front item in the deque always the highest block so far
    result = 0 
    # forward 
    i=0
    while i != len(height):
      if len(dq) == 0:
        dq.append(height[i])
      else: 
        if height[i] >= dq[0]:
          highestSoFar = dq[0]
          while len(dq) != 0:
            result+=(highestSoFar-dq[0])
            dq.popleft()
        dq.append(height[i])
      i+=1
    
    # backward (what left over is the part after height array behind the highest high)
    highestSoFar = 0
    while len(dq) != 0: 
      if dq[-1] >= highestSoFar:
        highestSoFar = dq[-1]
        dq.pop()
      else:
        result += (highestSoFar-dq[-1])
        dq.pop()
        
    return result
        
height = [4,2,0,3,2,5]
print(Solution().trap(height))        
      
        
      
      
      
    
    