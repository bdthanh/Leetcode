from typing import List
class Solution:
  def rob(self, nums: List[int]) -> int:
    def robUtil(nums: List[int]) -> int:
      if len(nums) == 0:
        return 0 
      if len(nums) == 1:
        return nums[0]
      if len(nums) == 2:
        return max(nums[0], nums[1])
      if len(nums) == 3:
        return max(nums[0] + nums[2], nums[1])
    
      dp = [0]*len(nums)
      dp[0] = nums[0]
      dp[1] = max(nums[0], nums[1])
      dp[2] = max(nums[0] + nums[2], nums[1])
      maxSoFar = max(dp[0], max(dp[1], dp[2]))
      for i in range(3, len(nums)):
        dp[i] = max(dp[i-2], dp[i-3]) + nums[i]
        maxSoFar = max(dp[i], maxSoFar)      
      return maxSoFar
    if len(nums) == 0:
      return 0 
    if len(nums) == 1:
      return nums[0] 
    case1 = robUtil(nums[0:len(nums)-1])
    case2 = robUtil(nums[1:len(nums)])
    return max(case1, case2)
  
nums = [2,3,2]
print(Solution().rob(nums))