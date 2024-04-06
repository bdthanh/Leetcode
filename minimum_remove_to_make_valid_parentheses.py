class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        ignore = set()
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            if c == ')':
                if len(stack)!= 0:
                    stack.pop()
                else:
                    ignore.add(i)
        for i in stack:
            ignore.add(i)
        ans = ''
        for i, c in enumerate(s):
            if i not in ignore:
                ans += c
        return ans
        