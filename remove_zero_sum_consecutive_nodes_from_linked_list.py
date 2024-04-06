from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        have = set()
        have.add(0)
        cur = head
        stack = [(0, -1)]
        curSum = 0
        id = 0
        while cur != None:
            curSum += cur.val
            if curSum in have:
                while len(stack) != 0 and stack[-1][0] != curSum:
                    pair = stack.pop()
                    have.remove(pair[0])
            else:
                stack.append((curSum, id, cur.val))
                have.add(curSum)
            id += 1
            cur = cur.next

        ans = ListNode(0, None)
        cur = ans
        id = 0
        for pair in stack:
            if pair[1] == -1:
                continue
            newNode = ListNode(pair[2], None)
            cur.next = newNode
            cur = cur.next
        return ans.next

        
  