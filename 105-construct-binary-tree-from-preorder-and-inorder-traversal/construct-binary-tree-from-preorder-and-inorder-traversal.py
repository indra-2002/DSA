# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inordermap={val: i for i, val in enumerate(inorder)}
        pre_idx=[0]
        def construct(left,right):
            if left > right:
                return None

            root_val=preorder[pre_idx[0]]
            pre_idx[0]+=1
            root=TreeNode(root_val)
            mid=inordermap[root_val]
            root.left=construct(left,mid-1)
            root.right=construct(mid+1,right)

            return root
        return construct(0,len(inorder)-1)