# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    count = 0
    iter1 = head
    while iter1 != None:
      count+=1
      iter1 = iter1.next
    prev = None  
    iter2 = head
    while count > n:
      count-=1
      prev = iter2
      iter2 = iter2.next
    next = iter2.next
    if prev == None:
      return head.next
    prev.next = next
    return head