# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        heap=[]
        for i , node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val,i , node))
        dummy=ListNode()
        curr=dummy
        while heap:
            val,i,node=heapq.heappop(heap)
            curr.next=node
            curr=node
            node=node.next
            if node:
                heapq.heappush(heap, ( node.val, i , node))
        return dummy.next