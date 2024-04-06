class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if len(stack) == 0: 
                stack.append(c)
                continue
            if ord(c) == ord(stack[-1]) + 32 or ord(c) == ord(stack[-1]) - 32:
                stack.pop()
            else: 
                stack.append(c)
        ans = ''
        for c in stack:
            ans+=c
        return ans