from typing import Optional
# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def reorderList(self, head: Optional[ListNode]) -> None:
    def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
      count = 0
      tempHead = head
      while tempHead != None:
        count += 1
        tempHead = tempHead.next
      count = count/2 if count%2==0 else int(count/2)+1
      while count != 0:
        count -= 1
        prev = head
        head = head.next
        if count == 0:
          prev.next = None #disconnect 2 linked list
      return head
      
    
    def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
      prev = None
      cur = head
      while cur != None:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
      return prev
    
    def merge(head1: Optional[ListNode], head2: Optional[ListNode]) -> None:
      while head2 != None:
        next1 = head1.next
        temp = head2
        head2 = head2.next
        head1.next = temp
        temp.next = next1 
        head1 = next1
    
    head2 = middleNode(head)
    head2 = reverseList(head2)
    newHead = head
    merge(head, head2)
    
    return newHead
  
temp = head = ListNode(1)
temp.next = ListNode(2)
temp = temp.next
temp.next = ListNode(3)
temp = temp.next
temp.next = ListNode(4)
temp = temp.next
head = Solution().reorderList(head)
while head != None:
  print(head.val)
  head = head.next