from typing import List
#O(n) space complexity
class Solution1:
  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    answer = [0] * len(temperatures)
    stack = []
    for i in range(len(temperatures)):
      while len(stack) != 0 and stack[-1][0] < temperatures[i]:
        answer[stack[-1][1]] += i - stack[-1][1]
        stack.pop()
      stack.append([temperatures[i],i])
    return answer
    
temperatures = [64,40,49,73,72,35,68,83]
print(Solution().dailyTemperatures(temperatures))