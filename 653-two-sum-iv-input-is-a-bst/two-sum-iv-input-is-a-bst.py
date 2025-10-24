# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums=[]
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)
        inorder(root)

        l=0
        r=len(nums)-1
        while l< r:
            if nums[l]+nums[r] > k:
                r-=1
            elif nums[l]+ nums[r]==k:
                return True

            else:
                l+=1

        return False