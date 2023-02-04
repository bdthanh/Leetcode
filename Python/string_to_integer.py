class Solution:
  def myAtoi(self, s: str) -> int:
    result = 0
    s = s.lstrip()
    if len(s) == 0:
      return 0
    def isIntegerChar(s: str, id: int) -> bool:
      if 48 <= ord(s[id]) <= 57:
        return True
      return False
    
    def isValidFirstChar(s: str) -> bool:
      asc = ord(s[0])
      if 48 <= asc <= 57 or asc == 43 or asc == 45:
        return True
      return False
    
    def getSign(s: str) -> int:
      if not isValidFirstChar(s):
        return 0
      if ord(s[0]) == 43:
        return 1  #postive
      if ord(s[0]) == 45:
        return -1 #negative 
      return 2 #default is positive and the first char is number
    
    sign = getSign(s)
    if sign == 0:
      return 0
    i = 0
    if (sign == 1 or sign == -1):
      i = 1
    if sign == 2: 
      sign = 1
    while i < len(s) and isIntegerChar(s, i):
      result *= 10
      result += (ord(s[i]) - 48)*sign
      print(result)
      if (result > 2**31-1):
        result = 2**31-1
        return result
      elif (result < -2**31):
        result = -2**31
        return result
      i+=1
    return result
  
s = "-423209482039908"
print(Solution().myAtoi(s))

