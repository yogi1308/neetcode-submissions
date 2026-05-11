# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)
        
        def insert(root, val, parent):
            if not root:
                if val < parent.val: parent.left = TreeNode(val)
                else: parent.right = TreeNode(val)
                return root

            if val < root.val: insert(root.left, val, root)
            else: insert(root.right, val, root)

        
        insert(root, val, None)

        return root