# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        dummy=curr
        l=0
        while curr:
            l+=1
            curr=curr.next

        m=0
        mid=l//2
        while m<mid:
            dummy=dummy.next
            m+=1
        return(dummy)
        