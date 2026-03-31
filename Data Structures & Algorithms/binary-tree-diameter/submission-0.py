# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # NEED TO DECLARE A VARIABLE THAT WILL HAVE THE RESULT
        diameter = [0]

        # CREATE A DFS FUNCTION THAT WILL COUNT THE HEIGHT OF EACH SIDE
        def dfs(node):
            # BASE CASE
            if not node:
                return 0

            # WE NEED TO COMPUTE THE HEIGHT OF LEFT AND RIGHT SIDE
            left = dfs(node.left)
            right = dfs(node.right)

            # WE NEED TO UPDATE THE DIAMETER
            diameter[0] = max(diameter[0], left + right)

            # RETURN THE HEIGHT
            return 1 + max(left, right)

        dfs(root)

        return diameter[0]

        