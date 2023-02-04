from typing import List
class Solution:
  def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    # count the number of occurences:
    count = {}
    for num in nums:
      if count.get(num) == None:
        count[num] = 1
      else:
        count[num] += 1
    # generate permutation 
    ans = []
    permutation = []
    def generatePermutation(permutation: List[int], count) -> None:
      if len(permutation) == len(nums):
        ans.append(permutation.copy())
      for num in count:
        if count[num] != 0:
          permutation.append(num)
          count[num]-=1
          generatePermutation(permutation, count)
          permutation.pop()
          count[num] += 1
    generatePermutation(permutation, count)
    return ans
  
nums = [1,1,2]
print(Solution().permuteUnique(nums))