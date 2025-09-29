# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        fast=slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        while slow!=None:
            nextpointer=slow.next
            slow.next=prev
            prev=slow
            slow =nextpointer
        left=head
        right=prev
        while right!=None:
            if left.val != right.val:
                return False
            else:
                left=left.next
                right=right.next
        return True
