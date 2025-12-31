'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def topView(self, root):
        # code here
        from collections import deque
        q=deque()
        q.append((root,0))
        map={}
        while q:
            node,col=q.popleft()
            if col not in map:
                map[col]=node.data
            if node.left:
                q.append((node.left,col-1))
            if node.right:
                q.append((node.right,col+1))
        return [map[x] for x in sorted(map)]
        
        