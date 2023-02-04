# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
class Solution(object):
  def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    r_val_copy = r_val = ListNode()
    add_one = 0
    while (l1 != None or l2 != None):
      sum = 0
      if l1 != None: 
        sum += l1.val
        l1 = l1.next
      if l2 != None: 
        sum += l2.val
        l2 = l2.next
      sum += add_one
      cur = sum % 10
      if (sum >= 10):
        add_one = 1
      else:
        add_one = 0
      cur_listNode = ListNode(cur)
      r_val.next = cur_listNode
      r_val = r_val.next
    
    if add_one == 1: 
      r_val.next = ListNode(1)
      r_val = r_val.next
    return r_val_copy.next