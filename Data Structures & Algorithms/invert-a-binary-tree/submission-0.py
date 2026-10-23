# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        result = []
        if not root:
            return
        # current = left value
        # left value = right // left is right
        # right = current // right is left
        current = root.left
        root.left = root.right
        root.right = current
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        