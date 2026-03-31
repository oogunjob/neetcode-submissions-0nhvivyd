# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        # need to return the height and if is balanced
        # if the node is none, then height is 0 and isBalanced is true

        # need to also check the abs(left and right) is not great than 1
        def checkBalanced(node):

            if not node:
                return [0, True]

            left_height, left_isBalanced = checkBalanced(node.left)
            right_height, right_isBalanced = checkBalanced(node.right)

            if not left_isBalanced or not right_isBalanced:
                return [0, False]

            isBalanced = abs(right_height - left_height) <= 1

            return [1 + max(left_height, right_height), isBalanced]

        height, isBalanced = checkBalanced(root)
        return isBalanced
        
