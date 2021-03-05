# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root, ct):
            if not root:
                return
            left = helper(root.left, ct)
            right = helper(root.right, ct)
            
            if root == p:
                ct[0] += 1
                return root
            elif root == q:
                ct[1] += 1
                return root
            if left and right:
                return root
            else:
                return left or right
            
        ct = [0,0]
        res = helper(root, ct)
        if not ct[0] or not ct[1]:
            return
        return res