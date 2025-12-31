'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def boundaryTraversal(self, root):
        # code here
        res=[]
        res.append(root.data)
        def left1(root):
            if not root or (not root.left and not root.right):
                return 
            res.append(root.data)
            if root.left:
                left1(root.left)
            else:
                left1(root.right)
        def leaves(root):
            if not root:
                return
            leaves(root.left)
            if not root.left and not root.right:
                res.append(root.data)
            leaves(root.right)
        def right1(root):
            if not root or (not root.right and not root.left):
                return
            
            if root.right:
                right1(root.right)
            else:
                right1(root.left)
            res.append(root.data)
        left1(root.left)
        leaves(root.left)
        leaves(root.right)
        right1(root.right)
        return res
                
            
            