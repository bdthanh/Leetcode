from typing import List

class Solution1: #TLE
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        height = len(nums)
        width = 0
        for arr in nums: 
            width = max(width, len(arr))
        iter_num = height+width-1
        ans = []
        for i in range(iter_num):
            for j in range(i+1):
                k = i - j
                if k >= height:
                    continue
                if j >= len(nums[k]):
                    continue
                ans.append(nums[k][j])
        return ans
      
class Solution2:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        flatten = []
        for i, arr in enumerate(nums):
            for j, num in enumerate(arr):
                flatten.append((i+j, i, num))
        ans = [i[2] for i in sorted(flatten, key=lambda tup: (tup[0], -tup[1]))]
        return ans 