# should shorten the code
class Solution:
  def countDigitOne(self, n: int) -> int:
    count = 0
    if n == 0: 
      return 0
    for i in range(1,len(str(n))+1): 
      tenPowerI = pow(10, i)
      tenPowerIMinus = pow(10, i-1)
      nearest = int(n / tenPowerI)*tenPowerI + 1 * tenPowerIMinus
      if nearest > n:
        nearest -= tenPowerI
      count += (int((nearest - tenPowerIMinus)/tenPowerI) + 1)*tenPowerIMinus
      if int(n/tenPowerIMinus)%10 == 1:
        count = count - tenPowerIMinus + n - nearest + 1
    return count
  
n = 10
print(Solution().countDigitOne(n))
      
      