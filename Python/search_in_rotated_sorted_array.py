from typing import List
class Solution:
  def search(self, nums: List[int], target: int) -> int:
    def binarySearch(beg: int, end: int) -> int:
      if beg == end:
        if nums[beg] == target:
          return beg
        return -1
      mid = int((beg+end)/2)
      if nums[beg] <= target <= nums[mid] or (nums[mid+1] <= nums[end] and (target < nums[mid+1] or target > nums[end])):
        return binarySearch(beg, mid)
      return binarySearch(mid+1, end)
      
    return binarySearch(0, len(nums)-1)
  
  
nums = [4,5,6,7,8,1,2,3]
target = 8
print(Solution().search(nums, target))