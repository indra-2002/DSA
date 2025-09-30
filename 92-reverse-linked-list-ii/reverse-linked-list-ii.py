# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        dummy.next=head
        curr=head
        leftprev=dummy
        for i in range(left-1):
            leftprev=leftprev.next
            curr=curr.next
        leftstart=curr
        prev=None
        for i in range(right-left+1):
            nextpointer=curr.next
            curr.next=prev
            prev=curr
            curr=nextpointer
        leftprev.next=prev
        leftstart.next=nextpointer
        return dummy.next
        
        


            