# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi=[float('-inf')]
        def maxim(root):

            if not root:
                return 0
            left=max(0,maxim(root.left))
            right=max(0,maxim(root.right))
            maxi[0]=max(maxi[0],root.val+left+right)

            return root.val+ max(left,right)
        maxim(root)
        return maxi[0]