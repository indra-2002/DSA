# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N=0
        curr=head
        while curr:
            N+=1
            curr=curr.next
        curr=head
        if n==N:
            return head.next
        for _ in range(N-n-1):
            curr=curr.next
        curr.next=curr.next.next
        return head
            
