from collections import OrderedDict
#sliding window optimized (use 2 windows) 
class Solution:
  def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
    d = OrderedDict()
    max_count, i, j = 0, 0, 0
    if k == 0:
       return 0
    while i < len(s):
      if d.get(s[i]) == None and len(d) == k: 
        max_count = max(i - j,max_count)
        j = d[next(iter(d))]+1
        d.popitem(last=False)
      d[s[i]] = i
      d.move_to_end(s[i])
      i+=1
    return max(i-j, max_count)

s = "ccaabbb"
print(Solution().lengthOfLongestSubstringKDistinct(s, 2))                   
                  