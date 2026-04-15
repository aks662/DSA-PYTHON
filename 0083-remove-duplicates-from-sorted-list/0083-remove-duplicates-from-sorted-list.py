# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head 
    

        while  curr!=None and curr.next!=None:
            end=curr.next

            while end!=None and curr.val==end.val  :
                end=end.next
            curr.next=end
            curr=curr.next
            
            

        return head
        