# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prev=dummy
        curr=head
        while curr and curr.next:
            npn=curr.next.next
            np=curr.next

            np.next=curr
            curr.next=npn
            prev.next=np

            prev=curr
            curr=npn
        return dummy.next