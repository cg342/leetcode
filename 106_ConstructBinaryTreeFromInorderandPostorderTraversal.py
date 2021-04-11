class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return
        rootvalue = postorder[-1]
        root = TreeNode(rootvalue)
        ind = inorder.index(rootvalue)
        
        root.left = self.buildTree(inorder[:ind], postorder[:ind])
        root.right = self.buildTree(inorder[ind+1:], postorder[ind:-1])
        
        return root