from typing import List
class Solution:
  def firstMissingPositive(self, nums: List[int]) -> int:
    # the answer is in the range of len(nums) - the number of 0's and negative numbers
    # check the visited number by a float
    # if there is number i then nums[i-1] = 1.5 
    # O(n)
    for i in range(len(nums)):
      if nums[i] == -1:
        nums[i] = -2
    i = 0
    while i < len(nums):
      cur = nums[i]
      while cur != -1:
        if 0 <= cur-1 < len(nums):
          temp = nums[cur-1]
          nums[cur-1] = -1
          if temp-1 == cur and nums[cur] == -1:
            break
          cur = temp
        else:
          break
      i+=1
    # find the missing one: O(n)
    j = 0
    while j < len(nums) and nums[j] == -1: # nums[j] == 1.5 if there is number j+1 in the original list
      j+=1
    return j+1
  
nums = [98,93,95,10,91,4,90,88,56,84,65,62,83,80,78,60,73,77,76,29,63,12,57,17,69,68,50,11,31,33,8,42,38,7,0,37,48,26,20,44,46,43,52,51,47,18,49,58,2,39,30,81,22,55,36,40,15,27,21,32,64,41,53,19,28,24,9,25,3,59,66,82,61,70,23,34,71,54,74,-1,1,45,14,79,5,35,13,72,75,85,87,6,16,86,67,89,94,92,96,97]
print(Solution().firstMissingPositive(nums))
    