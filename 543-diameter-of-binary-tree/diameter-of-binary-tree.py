# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=[0]
        def height(root):
            if not root:
                return 0
            l=height(root.left)
            r=height(root.right)
            diameter[0]=max(diameter[0],l + r)
            return 1+max(l,r)
        height(root)
        return diameter[0]

        