# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        self.stk=[]
        self.push(root)
    def push(self,root):
        while root:
            self.stk.append(root)
            root=root.left
    def next(self) -> int:
        node = self.stk.pop()
        if node.right:
            self.push(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stk)>0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()