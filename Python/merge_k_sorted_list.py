from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]: 
    def merge2Lists(list1: ListNode, list2: ListNode) -> Optional[ListNode]:
      newListReturn = newList = ListNode()
      while list1 != None or list2 != None:
        if list1 == None:
          newList.next = ListNode(list2.val)
          newList = newList.next
          list2 = list2.next
          continue
        if list2 == None:
          newList.next = ListNode(list1.val)
          newList = newList.next
          list1 = list1.next
          continue
        if list1.val <= list2.val:
          newList.next = ListNode(list1.val)
          newList = newList.next
          list1 = list1.next
        else:
          newList.next = ListNode(list2.val)
          newList = newList.next
          list2 = list2.next
      return newListReturn.next
    
    if len(lists) == 0:
      return None
    while len(lists) != 1:
      newLists = []
      i=0
      while i+1 < len(lists):
        newLists.append(merge2Lists(lists[i], lists[i+1]))
        i+=2
      if len(lists)%2==1:
        newLists.append(lists[-1])
      lists = newLists
        
    return lists[0]