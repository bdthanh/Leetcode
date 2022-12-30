# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution1:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      oriList = []
      if head == None: 
        return None
      while head != None:
        oriList.append(head.val)
        prev = head
        head = head.next
        del prev
      oriList = sorted(oriList)
      ans = sortedList = ListNode()
      for num in oriList:
        sortedList.next = ListNode(num)
        sortedList = sortedList.next
      return ans.next
        
class Solution:
  def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    pass
        