class Solution:
  def minimumPartition(self, s: str, k: int) -> int:
    curNum = 0
    i = 0
    counter = 0
    while i < len(s):
      if int(s[i]) > k:
        return -1
      while i < len(s):
        curNum = curNum*10+int(s[i])
        if curNum > k:
          break
        i+=1
      counter+=1  
      curNum = 0
    return counter

s = "165462"
k = 60
print(Solution().minimumPartition(s, k))
        