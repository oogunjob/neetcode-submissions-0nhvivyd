class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # RAWBIDI
        # REPEAT THE QUESTION
        # ASK CLARITICATION
        # WORK THROUGH AN EXAMPLE
        # BRAINSTORM SOLUTION
        # ASK FOR GO AHEAD
        # IMPLEMENT SOLUTION
        # DEBUG
        # IMPROVE

        # TIME COMPLEXITY: O(N)
        # SPACE COMPLEXITY: O(N)

        # [2, 20, 4, 10, 3, 4, 5]

        # need to keep track of the max sequence length

        if not nums:
            return 0

        longest_consecutive = 0
        num_set = set(nums) # O(N)

        for num in num_set:

            if num - 1 not in num_set:
                current_streak = 1
                val = num

                while val + 1 in num_set:
                    current_streak += 1
                    val += 1

                longest_consecutive = max(longest_consecutive, current_streak)

        return longest_consecutive