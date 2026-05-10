# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        l1 = list1
        l2 = list2
        if l1 == None :
            return l2
        if l2 == None :
            return l1

        arr = ListNode(0) 
        ans = arr
        while l1 and l2 :
            if l1.val < l2.val :
                nxt = l1.next
                arr.next = l1 
                arr = arr.next
                l1 = nxt
            else:
                nxt = l2.next 
                arr.next = l2
                arr = arr.next
                l2 = nxt
        while l2 :
            arr.next = l2
            arr = arr.next
            l2 = l2.next
        while l1 :
            arr.next = l1
            arr = arr.next
            l1 = l1.next

        return ans.next
