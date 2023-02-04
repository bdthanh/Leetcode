class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    dic = {}
    for c in s: 
      if c in dic:
        dic[c] += 1
      else:
        dic[c] = 1
        
    for c in t:
      if not c in dic:
        return False
      else: 
        dic[c] -= 1
        if dic[c] < 0:
          return False
    for item in dic:
      if dic[item] != 0:
        return False
    return True
  
s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))