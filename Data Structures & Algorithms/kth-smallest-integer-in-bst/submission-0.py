# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # RAWBIDI
        # REPEAT THE QUESTION
        # ASK FOR CLARIFICATION
        # WORK THROUGH AN EXAMPLE
        # BRAINSTORM SOLUTION
        # IMPLEMENT SOLUTION
        # DEBUG
        # IMPROVE

        # TIME COMPLEXITY: O(N) ITERATE OVER EVERY VALUE IN THE TREE
        # SPACE COMPLEXITY: O(N) USING A HEAP TO STORE THE VALUES

        heap = []
        

        def addNodes(node):
            if not node:
                return

            heap.append(node.val)
            addNodes(node.left)
            addNodes(node.right)

        addNodes(root)
        heapq.heapify(heap) # O(LOG N)

        i = 0
        while i < k - 1:
            heapq.heappop(heap)
            i += 1

        return heap[0]
        
        