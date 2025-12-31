# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def ancestor(root,mini,maxi):
            if not root:
                return maxi-mini
            mini=min(mini,root.val)
            maxi=max(maxi,root.val)
            left=ancestor(root.left,mini,maxi)
            right=ancestor(root.right,mini,maxi)

            return max(left,right)
        return ancestor(root,root.val,root.val)
            
        