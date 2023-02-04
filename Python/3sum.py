from typing import List
class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    ans = []
    visited = set()
    for i in range(len(nums)):
      if not nums[i] in visited:
        cur = -nums[i]
        match = set()
        seen = set()
        for j in range(len(nums)):
          if not nums[j] in visited and j != i and not nums[j] in seen:
            if nums[j] in match:
              ans.append([-cur, nums[j], cur - nums[j]])
              seen.add(nums[j])
              seen.add(cur-nums[j])
            else:
              match.add(cur - nums[j])
        visited.add(nums[i])
    return ans
  
nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))
            