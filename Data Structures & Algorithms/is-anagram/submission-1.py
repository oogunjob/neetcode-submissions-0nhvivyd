from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # RAWBIDI
        # REPEAT THE QUESTION
        # ASK CLARIFICATION (ASSUMPTIONS, CONSTRAINTS, EDGE CASES)
        # WORK THROUGH AN EXAMPLE
        # BRAINSTORM SOLUTION
        # ASK FOR GO-AHEAD
        # IMPLEMENT SOLUTION
        # DEBUG
        # IMPROVE

        # PATTERN:

        # TIME COMPLEXITY: O(1)
        # SPACE COMPLEXITY: O(N)

        
        # IF THEY'RE NOT THE SAME LENGTH, RETURN FALSE
        # IF CASING DID MATTER, LOWER BOTH OF THEM
        if len(s) != len(t):
            return False

        counter_s = Counter(s)
        counter_t = Counter(t)

        return counter_s == counter_t
