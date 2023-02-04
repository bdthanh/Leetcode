from typing import List
class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
    ans = []
    def generatePermutation(curSwap) -> None:
      if curSwap == len(nums):
        ans.append(nums.copy())
      for i in range(curSwap, len(nums)):
        nums[curSwap], nums[i] = nums[i], nums[curSwap]
        generatePermutation(curSwap+1)
        nums[curSwap], nums[i] = nums[i], nums[curSwap]
    generatePermutation(0)
    return ans

nums = [1, 2 ,3]
print(Solution().permute(nums))