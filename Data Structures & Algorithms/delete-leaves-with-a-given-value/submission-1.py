# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        mamaRoot = root
        def dfs(root, parent, dir):
            if not root: return
            if root and not root.left and not root.right and root.val == target: 
                nonlocal mamaRoot
                if dir == "left": parent.left = None
                elif dir == "right": parent.right = None
                else: mamaRoot = None
                removed = True
                print(removed)
                dfs(mamaRoot, None, None)
            if root: dfs(root.left, root, "left")
            if root: dfs(root.right, root, "right")
        dfs(mamaRoot, None, None)
        return mamaRoot
