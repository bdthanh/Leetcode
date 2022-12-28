from typing import List 
class Solution:
  def minCostClimbingStairs(self, cost: List[int]) -> int:
    costSoFar = [0] * len(cost)
    if len(cost) <= 1:
      return 0 
    costSoFar[0]=cost[0]
    costSoFar[1]=cost[1]
    for i in range(2, len(cost)):
      costSoFar[i] = min(costSoFar[i-2]+cost[i], costSoFar[i-1]+cost[i])
    return min(costSoFar[-1], costSoFar[-2])
  
cost = [1,100,1,1,1,100,1,1,100,1]
print(Solution().minCostClimbingStairs(cost))
      