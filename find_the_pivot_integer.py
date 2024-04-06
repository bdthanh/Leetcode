class Solution:
    def pivotInteger(self, n: int) -> int:
        front = 0
        for i in range(1,n+1):
            front += i
        back = 0
        for i in range(1,n+1):
            front -= (i-1)
            back += i
            if front == back: 
                return i
        return -1