# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head==None:
            return head
        if head.next==None:
            return head

        curr=head

        dummy=head
        l=1

            
        while dummy.next is not None:
            l+=1
            dummy=dummy.next
        dummy.next=curr
        
        rotate=k%l
        position = l - rotate

        

        ans=ListNode(0)
        for i in range(position-1):
            curr=curr.next
        ans=curr.next
        curr.next=None


        return ans


        



        

        