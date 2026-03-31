class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # RAWBIDI
        # REPEAT THE QUESTION
        # ASK CLARIFICATION
        # WORK THROUGH AN EXAMPLE
        # BRAINSTORM SOLUTION
        # ASK FOR GO-AHEAD
        # IMPLEMENT SOLUTION
        # DEBUG
        # IMPROVE

        # PATTERN

        # TIME COMPLEXITY:
        # SPACE COMPLEXITY:
        
        hashmap = {}

        for i, num in enumerate(nums):
            difference = target - num
            if difference in hashmap:
                return [hashmap[difference], i]

            hashmap[num] = i

        return []