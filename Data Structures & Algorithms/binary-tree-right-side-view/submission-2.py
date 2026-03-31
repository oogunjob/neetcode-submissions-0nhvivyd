# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # RAWBIDI
        # REPEAT THE QUESTION
        # ASK CLARIFICATION
        # WORK THROUGH AN EXAMPLE
        # BRAINSTORM SOLUTION
        # ASK FOR GO AHEAD
        # IMPLEMENT SOLUTION
        # DEBUG
        # IMPROVE

        # TIME COMPLEXITY: O(H)
        # SPACE COMPLEXITY: O(N)

        if not root:
            return []

        # DECLARE A QUEUE AND AN OUTPUT ARRAY
        # THE QUEUE WILL HOLD EACH NODE WE'RE VISITING
        # THE OUTPUT ARRAY WILL HOLD EACH NODE THAT IS SEEN FROM THE RIGHT SIDE
        
        # THE ROOT WILL ALWAYS BE SEEN
        # EDGE CASE: IF THERE IS NO ROOT, JUST RETURN NONE

        # ITERATE THROUGH THE QUEUE
        # FOR EACH ONE IN THERE
        
        # IF THE NODE HAS A NODE.RIGHT:
        # ONLY ADD ((THAT)) TO THE ((((OUTPUT)))) ARRAY
        # WE WILL STILL NEED TO ADD IT'S SIBILING THROUGH THE QUEUE JUST IN CASE
        # IF IT DIDN'T HAVE NODE.RIGHT, THEN CHECK IF THE SIBLING HAS A NODE.RIGHT
        # IF THE SIBLING DOES HAVE A NODE.RIGHT INCLUDE IT IN THE OUTPUT
        # IF IT DOESN'T HAVE A NODE.RIGHT BUT IT HAS A NODE.LEFT THEN INCLUDE THAT IN THE OUTPUT

        # DECLARE THE QUEUE AND OUTPUT
        q = collections.deque()
        output = []
        q.append(root)

        while q:
            level = []
            for _ in range(len(q)):
                # FETCH THE LATEST NODE FROM THE QUEUE
                node = q.popleft()

                level.append(node.val)

                if node.right:
                    q.append(node.right)

                if node.left:
                    q.append(node.left)

            if level:
                output.append(level[0])

        return output