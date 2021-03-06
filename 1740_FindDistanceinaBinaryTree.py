# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        def findLCA(root):
            if not root:
                return 
            if root.val == p or root.val == q:
                return root
            left = findLCA(root.left)
            right = findLCA(root.right)
            
            if left and right:
                return root
            else:
                return left or right
        
        def distance(node, target):
            if not node:
                return float('inf')
            if node.val == target:
                return 0
            return min(distance(node.left, target), distance(node.right, target)) + 1
        
        lca = findLCA(root)
        return distance(lca, p) + distance(lca, q)
            
        
        