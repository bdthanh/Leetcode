class Solution:
  def myPow(self, x: float, n: int) -> float:
    if n == 0:
      return 1
    if x == 0:
      return 0
    elif (n < 0):
      x = 1/x
      n = abs(n)
    r = x
    i = 1
    while i*2 < n:
      r*=r
      i*=2
      
    return r*Solution().myPow(x, n-i)
  
print(Solution().myPow(2, 10))