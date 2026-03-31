# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # I NEED TO DEVELOP A HELPER FUNCTION THAT WILL DETERMINE WHETHER A TREE IS THE SAME OR NOT
        def isSameTree(p, q):
            if not q and not p:
                return True

            if p and not q or q and not p:
                return False

            if p.left and not q.left or q.left and not p.left:
                return False

            if p.val != q.val:
                return False

            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


        def has_subtree(root):
            # CHECK IF THE ROOT EXISTS
            if not root:
                return False

            # CHECK IF THE ROOT/SUBROOT ARE THE SAME
            if isSameTree(root, subRoot):
                return True

            # CHECK IF ROOT.LEFT OR ROOT.RIGHT / SUBROOT ARE THE SAME
            return has_subtree(root.left) or has_subtree(root.right)
        
        return has_subtree(root)
