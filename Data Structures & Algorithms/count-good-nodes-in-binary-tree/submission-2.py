# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        vals = 0
        def fn(root, maxVal):
            if not root: return
            if root.val >= maxVal:
                nonlocal vals
                vals += 1
                maxVal = root.val
            
            fn(root.left, maxVal)
            fn(root.right, maxVal)
            return

        fn(root, float('-inf'))
        return vals