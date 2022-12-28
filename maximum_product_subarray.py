from typing import List
class Solution1:
  def maxProduct(self, nums: List[int]) -> int:
    if len(nums) == 1:
      return nums[0]
    maxProduct = -2147483648
    curProduct = 1
    zeroPos = []
    
    zeroPos.append(-1)
    for i in range(len(nums)):
      if nums[i] == 0:
        zeroPos.append(i)
    zeroPos.append(len(nums))
    
    for i in range(len(zeroPos)-1):
      #subarray removed 0
      start = zeroPos[i]+1
      end = zeroPos[i+1]-1
      if end == start-1:
        continue
      subProduct = 1
      if start == end and nums[start] < 0:
        subProduct = 0
        maxProduct = max(maxProduct, subProduct)
        continue
      
      for j in range(start, end+1):
        subProduct *= nums[j]
        
      if subProduct < 0:
        sub1, sub2 = subProduct, subProduct
        for k in range(start, end+1):
          sub1 /= nums[k]
          if nums[k] < 0:
            break
        for k in range(end, start-1, -1):
          sub2 /= nums[k]
          if nums[k] < 0:
            break
        subProduct = max(sub1, sub2)
      maxProduct = max(maxProduct, subProduct)
    return int(maxProduct)
  
class Solution2:
  def maxProduct(self, nums: List[int]) -> int:
    maxSoFar = nums[0]
    minSoFar = nums[0]
    ans = -2147483648
    for i in range(1, len(nums)):
      num = nums[i]
      tempMax = max(num, maxSoFar*num, minSoFar*num)
      minSoFar = min(num, maxSoFar*num, minSoFar*num)
      maxSoFar = tempMax
      ans = max(ans, maxSoFar)
    return ans
      
nums = [-2,0]
print(Solution1().maxProduct(nums))
print(Solution2().maxProduct(nums))