# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def getDepth(node):
            if not node:
                return 0
            left_height = getDepth(node.left)
            right_height = getDepth(node.right)
            return 1 + max(left_height, right_height)
        left_depth = getDepth(root.left)
        right_depth = getDepth(root.right)
        if abs(left_depth - right_depth) > 1:
            return False
        if self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False