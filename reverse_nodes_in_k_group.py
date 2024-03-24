# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        len = 0
        headc = head 
        while headc != None:
            len+=1
            headc = headc.next
        ngroups = int(len/k)

        def reverseGroup(prev_node, head_node):
            prev = None
            cur = head_node
            next = head_node.next
            new_end = head_node

            for i in range(k):
                cur.next = prev
                prev = cur
                cur = next
                next = next.next if next != None else None
            #head, next, end
            new_end.next = cur
            if prev_node != None:
                prev_node.next = prev
            return prev, cur, new_end

        next_head = None
        prev = None
        new_next_group = head
        for i in range(ngroups):
            new_head, new_next_group, prev = reverseGroup(prev,new_next_group)
            if i == 0:
                ans_head = new_head
        return ans_head