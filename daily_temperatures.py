from typing import List
#O(n) space complexity
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0 for i in range(len(temperatures))]
        for pair in enumerate(temperatures):
            while len(stack) != 0 and pair[1] > stack[-1][1]:
                distance = pair[0]-stack[-1][0]
                ans[stack.pop()[0]] = distance
            stack.append(pair)
        return ans
    
temperatures = [64,40,49,73,72,35,68,83]
print(Solution().dailyTemperatures(temperatures))