# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count=[0]
        self.result=None
        def smallest(root):
            if not root or self.result is not None:
                return 
            smallest(root.left)
            count[0]+=1
            if count[0]==k:
                self.result=root.val
                return 
            smallest(root.right)
        smallest(root)
        return self.result 