'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def isSumProperty(self, root):
        # code here
        if not root:
            return 1
        if not root.left and not root.right:
            return 1
        left = root.left.data if root.left else 0
        right = root.right.data if root.right else 0
        if root.data !=  left+ right:
            return 0
            
        return self.isSumProperty(root.left) and self.isSumProperty(root.right)
    
        
        
        