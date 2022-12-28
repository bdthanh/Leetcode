from typing import List
import random
class Solution:       
  def findKthLargest(self, nums: List[int], k: int) -> int:
    def quickSelect(beg: int, end: int) -> int:  
      pivotId = random.randint(beg, end-1)
      pivot = nums[pivotId]
      nums[pivotId], nums[beg] = nums[beg], nums[pivotId]
      wall = beg+1
      for i in range(beg+1, end):
        if nums[i] < pivot:
          nums[i], nums[wall] = nums[wall], nums[i]
          wall+=1
      nums[beg], nums[wall-1] = nums[wall-1], nums[beg]
      
      if len(nums)-wall+1 == k:
        return nums[wall-1]
      elif len(nums)-wall+1 < k:
        return quickSelect(beg, wall)
      return quickSelect(wall, end)
    
    return quickSelect(0, len(nums))

nums = [3,2,1,5,6,4]
k = 2
print(Solution().findKthLargest(nums, k))