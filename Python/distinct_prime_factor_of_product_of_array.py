from math import sqrt
from typing import List
class Solution:
  def distinctPrimeFactors(self, nums: List[int]) -> int:
    seen = set()
    for num in nums:
      i = 2
      while i*i <= num:
        while num%i == 0:
          num/=i
          seen.add(i)
        i+=1
      if num > 1:
        seen.add(num)
        
    return len(seen)
  
nums = [2,4,8,16]
print(Solution().distinctPrimeFactors(nums))
          
        
      