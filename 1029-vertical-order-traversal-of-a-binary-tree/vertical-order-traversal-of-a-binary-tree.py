# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        from collections import defaultdict,deque
        q=deque()
        q.append((root,0,0))
        nodes=[]
        while q:
            node,row,col=q.popleft()
            nodes.append((col,row,node.val))
            if node.left:
                q.append((node.left,row+1,col-1))
            if node.right:
                q.append((node.right,row+1,col+1))
        nodes.sort()
        res=defaultdict(list)
        for i,j,k in nodes:
            res[i].append(k)
        return [res[x] for x in sorted(res)]