class Solution:
    def lengthOfLastWord(self, s: str) -> int: 
        s = s[::-1]
        a = 0
        for id, char in enumerate(s):
            if char != " ":
                a=id
                break
        count = 0
        while a < len(s) and s[a] != " ":
            count += 1
            a+=1
        return count        