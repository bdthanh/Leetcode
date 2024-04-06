class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        max_count = 0
        for char in s:
            if char == '(':
                count+=1
            elif char == ')':
                count-=1
            max_count = max(count, max_count)
        return max_count