class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        if not preorder or not inorder:
            return
        rootvalue = preorder[0]
        root = TreeNode(rootvalue)
        ind = inorder.index(rootvalue)
        
        root.left = self.buildTree(preorder[1:ind+1], inorder[:ind])
        root.right = self.buildTree(preorder[ind+1:], inorder[ind+1:])
        
        return root