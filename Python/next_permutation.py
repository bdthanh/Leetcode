from typing import List
class Solution:
  def nextPermutation(self, nums: List[int]) -> None:
    i = len(nums)-1
    while i > 0:
      if (nums[i] > nums[i-1]):
        decID = i-1
        while i < len(nums) and nums[decID] < nums[i]:
          i+=1 # loop stop when nums[i] is <= nums[decID] --> nums[i+1] > nums[decID]
        # Swap
        tempDec = nums[decID]
        nums[decID] = nums[i-1]
        nums[i-1] = tempDec
        # Reverse the back of the list 
        nums[decID+1:len(nums)] = nums[decID+1:len(nums)][::-1]
        break
      if (i == 1): # when the whole array is in descending order
        nums[0:len(nums)] = nums[0:len(nums)][::-1]
      i-=1
      
nums = [3,2,1]
Solution().nextPermutation(nums)
print(nums)
        
        
          