'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def delNode(self, root, x):
        #code here 
        def findmin(root):
            left=root
            while left and left.left:
                left=left.left
            return left
        
        if not root:
            return None
        if root.data > x:
            root.left =self.delNode(root.left,x)
        elif root.data<x:
            root.right= self.delNode(root.right,x)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                min_val=findmin(root.right)
                root.data=min_val.data
                root.right=self.delNode(root.right,root.data)
        return root
                