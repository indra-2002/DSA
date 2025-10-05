# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        def merging(head):
            if head==None or head.next==None:
                return head
            middle = getmiddle(head)
            left = head
            right=middle.next
            middle.next=None

            lefthead=  merging(left)
            righthead= merging(right)
            return merge(lefthead,righthead)
        def getmiddle(head):
            slow=head
            fast=head.next
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            return slow
        def merge(left,right):
            dummy=ListNode(0)
            mergelist=dummy
            while left and right:
                if left.val < right.val:
                    mergelist.next=left
                    left=left.next
                else:
                    mergelist.next=right
                    right=right.next
                mergelist=mergelist.next
            if left:
                mergelist.next=left
            if right:
                mergelist.next=right
            return dummy.next
         
        return merging(head)