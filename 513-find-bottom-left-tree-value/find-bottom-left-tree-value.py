# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        '''maxi=[0]
        leftmost=[0]
        def height(root,level):
            if not root :
                return 
            if maxi[0]<level:
                maxi[0]=level
                leftmost[0]=root.val
            if root.left:
                height(root.left,level+ 1)
            if root.right:
                height(root.right, level + 1)
        height(root,0)
        lefti=leftmost[0]
        return lefti '''# 3 didn't pass
        if not root:
            return 
        q=deque()
        q.append(root)
        while q:
            node=q.popleft()
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return node.val
