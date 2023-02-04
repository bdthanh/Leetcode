from typing import List 
class Solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    def modifiedBinarySearchToFindBeg(nums: List[int], target: int, beg: int, end: int) -> int:
    # find the lower_bound
      if nums[beg] == target and beg != 0 and nums[beg-1] < target:
        return beg
      if nums[end] == target and end != 0 and nums[end-1] < target:
        return end
      elif nums[beg] == target and beg == 0: # end always >= beg
        return 0
      elif end - beg <= 1 and nums[beg] != target and nums[end] != target:
        return -1
      mid = int((beg + end)/2)
      if nums[mid] >= target:
        return modifiedBinarySearchToFindBeg(nums, target, beg, mid)
      return modifiedBinarySearchToFindBeg(nums, target, mid+1, end)
    
    def modifiedBinarySearchToFindEnd(nums: List[int], target: int, beg: int, end: int) -> int:
      # find the upper_bound
      if nums[beg] == target and beg != len(nums)-1 and nums[beg+1] > target:
        return beg
      if nums[end] == target and end != len(nums)-1 and nums[end+1] > target:
        return end
      elif nums[end] == target and end == len(nums)-1: # end always >= beg
        return len(nums)-1
      elif end - beg <= 1 and nums[beg] != target and nums[beg] != target:
        return -1
      mid = int((beg + end)/2)
      if nums[mid] <= target:
        return modifiedBinarySearchToFindEnd(nums, target, mid, end)
      return modifiedBinarySearchToFindEnd(nums, target, beg, mid)
      
    range = [-1,-1]
    if (len(nums) == 0):
      return range
    range[0] = modifiedBinarySearchToFindBeg(nums, target, 0, len(nums)-1)
    range[1] = modifiedBinarySearchToFindEnd(nums, target, 0, len(nums)-1)
    return range
  
l = [5,7,7,8,8,10]
print(Solution().searchRange(l, 8))
    