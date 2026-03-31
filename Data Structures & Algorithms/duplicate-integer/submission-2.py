from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # RAWBIDI
        # Repeat the question
        # Ask clarification (constraints, edge cases)
        # Work through an example
        # Brainstorm
        # Ask for go-ahead
        # Implement solution
        # Debug
        # Improve

        # Pattern:

        # Time Complexity: O(1)
        # Space Complexity: O(n)

        if len(nums) == 0:
            return False

        counter = Counter(nums)
        most_common = counter.most_common(1)
        return most_common[0][1] > 1


        