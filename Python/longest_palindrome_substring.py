class Solution:
  def longestPalindrome(self, s: str) -> str:
    longestLen = 0
    maxBeg = 0
    singleCenter = 0
    while singleCenter + int(longestLen/2) < len(s):
      halfLength = 0
      while singleCenter-halfLength >= 0 and singleCenter+halfLength < len(s) and s[singleCenter-halfLength] == s[singleCenter+halfLength]:
        halfLength+=1
      halfLength-=1
      if 2*halfLength+1 > longestLen:
        longestLen = 2*halfLength+1 
        maxBeg = singleCenter - halfLength
      singleCenter+=1
    doubleCeneter = int(longestLen/2)
    while doubleCeneter + int(longestLen/2)+1 < len(s):
      halfLength = 0
      while doubleCeneter-halfLength >= 0 and doubleCeneter+halfLength+1 < len(s) and s[doubleCeneter-halfLength] == s[doubleCeneter+halfLength+1]:
        halfLength+=1
      halfLength-=1
      if 2*halfLength+2 > longestLen:
        longestLen = 2*halfLength+2
        maxBeg = doubleCeneter - halfLength
      doubleCeneter+=1  
    return s[maxBeg:maxBeg+longestLen]    
      
    
s = "ijhjkhknhkh"
print(Solution().longestPalindrome(s))