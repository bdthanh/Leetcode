class Solution:
  def climbStairs(self, n: int) -> int:
    ways = [0]*(n+1)
    fibo[0] = 1
    if n == 0:
      return fibo[0]
    fibo[1] = 1
    if n == 1:
      return fibo[1]
    fibo[2] = 2
    if n == 2:
      return fibo[2]
    i = 2
    while i != n:
      i+=1
      fibo[i] = fibo[i-1]+fibo[i-2]
    return fibo[n]