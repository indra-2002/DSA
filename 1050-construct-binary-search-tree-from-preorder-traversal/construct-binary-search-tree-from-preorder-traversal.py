# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        pre=[0]
        def construct(bound):
            if pre[0]==len(preorder) or preorder[pre[0]]> bound:
                return 
            root_val=preorder[pre[0]]
            pre[0]+=1
            root=TreeNode(root_val)
            root.left=construct(root.val)
            root.right=construct(bound)
            return root
        return construct(float('inf'))