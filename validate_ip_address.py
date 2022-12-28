class Solution:
  def validIPAddress(self, queryIP: str) -> str:
    def isValidV4(queryIP: str):
      x = queryIP.split(".")
      if len(x) != 4:
        return False
      for xi in x:
        if not 0 < len(xi) <= 3:
          return False
        
        for char in xi:
          if ord(char) < 48 or ord(char) > 57:
            return False
          
        if int(xi) > 255 or int(xi) < 0:
          return False
        if len(xi) > 1 and xi[0] == "0":
          return False
      return True
      
      
    def isValidV6(queryIP: str):
      x = queryIP.split(":")
      if len(x) != 8:
        return False
      for xi in x:
        if not 1 <= len(xi) <= 4:
          return False
        for char in xi:
          if not (48 <= ord(char) <= 57 or 65 <= ord(char) <= 70 or 97 <= ord(char) <= 102):
            return False
      return True
      
    if isValidV4(queryIP):
      return "IPv4"
    elif isValidV6(queryIP):
      return "IPv6"
    return "Neither"
  
queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
print(Solution().validIPAddress(queryIP))
      
    