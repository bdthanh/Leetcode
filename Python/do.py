from typing import List
from math import log2, ceil
def solution(nums: List[int]):
  maxSoFar = -1000002
  dic = []
  count =  0
  for num in nums:
    dic.append(num)
    maxSoFar = max(num, maxSoFar)
    if maxSoFar + num > 0:
      rangePower = int(log2(maxSoFar + num))
      for i in range(rangePower+1):
        if pow(2, i) - num in dic:
          count+=1
  return count
  
nums = [-2, -1, 0, 1, 2]
print(solution(nums))
