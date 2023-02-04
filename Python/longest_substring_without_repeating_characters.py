#sliding window optimized (use 2 windows)
class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    d = {}
    count, max_count, i, j = 0, 0, 0, 0
    while i < len(s):
      if d.get(s[i]) != None and d[s[i]] >= j: 
        count = i - j
        if (count > max_count):
          max_count = count
        j = d[s[i]]+1
      d[s[i]] = i
      i+=1
    return max(i-j, max_count)
