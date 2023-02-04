from typing import List
from collections import defaultdict
class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagrams = defaultdict(list)
    for s in strs:
      counter = [0 for _ in range(26)]
      for char in s:
        counter[ord(char)-97]+=1
      anagrams[tuple(counter)].append(s)
      
    ans = []
    for counter in anagrams:
      words = []
      for word in anagrams[counter]:
        words.append(word)
      ans.append(words)
    return ans
        
      
strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))