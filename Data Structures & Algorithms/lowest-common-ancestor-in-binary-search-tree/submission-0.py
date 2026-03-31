# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # NEED TO FIND THE MOMENT WHERE THE SPLIT OCCURS
        current = root

        # RAWBIDI
        # REPEAT THE QUESTION
        # ASK CLARIFICATION (EDGE CASES, ASSUMPTIONS, CONSTRAINTS)
        # WORK THROUGH AN EXAMPLE
        # BRAINSTORM A SOLUTION
        # ASK FOR GO AHEAD
        # IMPLEMENT SOLUTION
        # DEBUG
        # IMPROVE

        # TIME COMPLEXITY:
        # SPACE COMPLEXITY:

        lowest_ancestor = None

        while current:
            if p.val < current.val and q.val < current.val:
                current = current.left

            elif p.val > current.val and q.val > current.val:
                current = current.right

            else:
                lowest_ancestor = current
                break

        return lowest_ancestor
        