from typing import List

#dynamic programming
class Solution1:
  def maxSubArray(self, nums: List[int]) -> int:
    if len(nums) == 0:
      return 0
    dp = [0]*len(nums)
    dp[0] = nums[0]
    maxSoFar = dp[0]
    for i in range(1, len(nums)):
      dp[i] = max(nums[i], dp[i-1] + nums[i])
      maxSoFar = max(maxSoFar, dp[i])
    return maxSoFar
  
#Kadane's algo

class Solution2:
  def maxSubArray(self, nums: List[int]) -> int:
    if len(nums) == 0:
      return 0
    maxSoFar = nums[0]
    curSubArraySum = 0
    for i in range(len(nums)):
      curSubArraySum = max(nums[i], curSubArraySum + nums[i]) 
      maxSoFar = max(maxSoFar, curSubArraySum)
    return maxSoFar
  
nums = [-1]
print(Solution1().maxSubArray(nums)) 
print(Solution2().maxSubArray(nums))    