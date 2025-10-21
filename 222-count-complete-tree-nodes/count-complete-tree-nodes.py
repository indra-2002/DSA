# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left=root
        leftheight=0
        while left:
            leftheight+=1
            left= left.left
        right=root
        rightheight=0
        while right:
            rightheight+=1
            right = right.right
        if leftheight==rightheight:
            return ( 2** rightheight)-1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
        