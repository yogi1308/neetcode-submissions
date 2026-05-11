# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        vals = 0
        def fn(root, parents):
            if not root: return
            print(root.val, parents)
            if root.val >= max(parents):
                nonlocal vals
                vals += 1
            
            fn(root.left, parents + [root.val])
            fn(root.right, parents + [root.val])
            return

        fn(root, [float('-inf')])
        return vals