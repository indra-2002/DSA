# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        neg=float('-inf')
        pos=float('inf')
        def valid(root,neg,pos):
            if not root :
                return True
            if neg>=root.val or root.val >= pos:   
                return False
            return valid(root.left,neg,root.val) and valid(root.right,root.val,pos)
        return valid(root,neg,pos)          