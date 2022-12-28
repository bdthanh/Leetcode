from collections import Counter
class Solution:
  def minWindow(self, s: str, t: str) -> str:
    minBeg, minEnd = 0,0
    minLength = 2147483647
    noSolution = True
    i,j=0,0
    lenS = len(s)
    counter = Counter(t)
    enough = set() #the substring contains all char in t when len(enough) == len(counter)
    while j < lenS:
      #expand
      while j < lenS and len(enough) != len(counter):
        if s[j] in counter:
          counter[s[j]] -= 1
          if counter[s[j]] <= 0:
            enough.add(s[j])
        j+=1
      if len(enough) == len(counter):
        noSolution = False
      #contract
      while i < j and len(enough) == len(counter):
        if s[i] in counter:
          counter[s[i]] += 1
          if counter [s[i]] > 0:
            enough.remove(s[i])
        i+=1
      if minLength > j-i+1:
        minLength = j-i+1
        minBeg = i-1
        minEnd = j     
    if noSolution:
      return "" 
    return s[minBeg:minEnd]
      
s = "ab"
t = "a"      
print(Solution().minWindow(s, t))
      