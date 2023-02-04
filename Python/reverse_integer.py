class Solution:
  def reverse(self, x: int) -> int:
    INT_MAX = 2**31-1
    INT_MIN = -2**31
    result = 0
    isNegetive = True if x < 0 else False
    x = abs(x)
    while x != 0:
      if (isNegetive and abs(INT_MIN)/10 < result) or (not isNegetive and INT_MAX/10 < result):
        return 0
      result = result*10 + x%10
      x = int(x/10)
      
    return -result if isNegetive else result
  
x = 2**31-1
print(Solution().reverse(x))