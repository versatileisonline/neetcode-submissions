# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 1. Create a variable to track the maximum diameter found so far
        self.max_diameter = 0
        
        # 2. Define a helper function to calculate the HEIGHT of a node
        def getHeight(node):
            if not node:
                return 0 # An empty node has a height of 0
            
            # Recursively get the heights of left and right subtrees
            left_height = getHeight(node.left)
            right_height = getHeight(node.right)
            
            # The longest path through THIS specific node is left + right
            # Update our global maximum if this path is longer than what we've seen
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            
            # Return the height of this node to its parent
            return 1 + max(left_height, right_height)
        
        # 3. Kick off the recursion starting at the root
        getHeight(root)
        
        # 4. Return the maximum diameter we tracked
        return self.max_diameter