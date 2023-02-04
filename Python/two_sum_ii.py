from typing import List
class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    low = 0
    high = len(numbers)-1
    while low != high:
      if numbers[low] + numbers[high] < target:
        low+=1
      elif numbers[low] + numbers[high] > target:
        high-=1
      else:
        break
    return [low, high]