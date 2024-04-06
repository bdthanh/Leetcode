class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = {}
        mapped = set()
        if len(s) != len(t):
            return False
        for i, char in enumerate(s): 
            if char not in m:
                m[char] = t[i]
                if t[i] in mapped:
                    return False
                mapped.add(t[i])
            else:
                if m[char] != t[i]:
                    return False
        return True 