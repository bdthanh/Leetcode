from typing import Optional
# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class SolutionIterative:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    cur = head
    while cur != None:
      next = cur.next
      cur.next = prev
      prev = cur
      cur = next
    return prev
  
class SolutionRecursion:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    cur = head
    def reverseUtil(prev, cur):
      if cur == None: 
        return prev
      next = cur.next
      cur.next = prev
      prev = cur
      cur = next
      return reverseUtil(prev, cur)
    return reverseUtil(prev, cur)
  
head = temp = ListNode(5)
temp.next = ListNode(4)
temp = temp.next
temp.next = ListNode(3)
temp = temp.next
temp.next = ListNode(2)
temp = temp.next
temp.next = ListNode(1)
temp = temp.next
ans = Solution().reverseList(head)
while ans != None:
  print(ans.val)
  ans = ans.next
