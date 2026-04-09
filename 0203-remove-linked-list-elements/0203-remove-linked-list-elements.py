# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node=ListNode(0)
        node.next=head
        curr=node
        while curr.next:
            if curr.next.val==val:
                curr.next=curr.next.next
                continue
            curr=curr.next
        return node.next
                
                

        