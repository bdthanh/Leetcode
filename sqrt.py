class Solution:
  def mySqrt(self, x: int) -> int:
    def findSqrt(x, beg, end):
      mid = int((beg+end)/2)
      if mid != 0 and (mid-1)*(mid-1) <= x < mid*mid:
        return mid-1
      
      if mid * mid > x:
         return findSqrt(x, beg, mid-1)
      return findSqrt(x, mid+1, end) # mid * mid <= x:
    
    if 0 <= x < 1:
      return 0
    return findSqrt(x,1,46341)
  
x = 0.5
print(Solution().mySqrt(x))