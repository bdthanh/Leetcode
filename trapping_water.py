from collections import deque
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        maxID = 0
        for pair in enumerate(height):
            if pair[1] > height[maxID]:
                maxID = pair[0]
        ans = 0
        cur_max = 0
        for i in range(0,maxID+1):
            if cur_max <= height[i]:
                cur_max = height[i]
            else: 
                ans += cur_max - height[i]
        cur_max = 0
        for i in range(len(height)-1, maxID-1, -1):
            if cur_max <= height[i]:
                cur_max = height[i]
            else: 
                ans += cur_max - height[i]
        return ans
        
height = [4,2,0,3,2,5]
print(Solution().trap(height))        
      
        
      
      
      
    
    