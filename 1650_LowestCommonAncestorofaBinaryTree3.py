"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1, q1 = p, q
        while p1 != q1:
            p1 = p1.parent if p1.parent else q
            q1 = q1.parent if q1.parent else p
        
        return p1