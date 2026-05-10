# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # middle of list 
        fast = head
        slow = head
        while fast != None and fast.next != None :
            slow = slow.next
            fast = fast.next.next

        curr = slow.next 
        slow.next = None
        # rev a list 
        rev = None
        while curr :
            nxt = curr.next 
            curr.next = rev
            rev = curr
            curr = nxt 
        # add rev and l1

        first = head 
        second = rev
        while second :
            t1 = first.next
            t2 = second.next

            first.next = second
            second.next = t1

            first = t1
            second = t2

        return head
        


        