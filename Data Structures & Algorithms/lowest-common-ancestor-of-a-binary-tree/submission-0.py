# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = root

        def hasNode(root, node):
            if not root: return False
            if root == node: return True
            return hasNode(root.left, node) or hasNode(root.right, node)
        
        def hasPAndQ(root, p, q):
            nonlocal lca
            lca = root
            
            leftAndP = hasNode(root.left, p)
            rightAndP = hasNode(root.right, p)
            leftAndQ = hasNode(root.left, q)
            rightAndQ = hasNode(root.right, q)
            if leftAndP and leftAndQ: hasPAndQ(root.left, p, q)
            elif rightAndP and rightAndQ: hasPAndQ(root.right, p, q)
            
            print(lca)

        hasPAndQ(root, p, q)
        return lca