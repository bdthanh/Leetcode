# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    count = 0
    res = tempHead = head
    while tempHead != None:
      count += 1
      tempHead = tempHead.next
    count = int(count/2)
    prev = None
    while count != 0:
      count -= 1
      prev = head
      head = head.next
      if count == 0:
        prev.next = head.next # remove
    return res