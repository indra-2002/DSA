# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inordermap={val : i for i,val in enumerate(inorder)}
        postidx=[len(postorder)-1]
        def construct(left,right):
            if left> right:
                return None
            root_val=postorder[postidx[0]]
            postidx[0]-=1
            root=TreeNode(root_val)
            mid=inordermap[root_val]  
            root.right=construct(mid+1, right)
            root.left=construct(left,mid-1)
            return root
        return construct(0,len(inorder)-1)