class Solution:
    def findMin(self, nums: List[int]) -> int:
        # RAWBIDI
        # REPEAT THE QUESTION
        # ASK CLARIFICATION (EDGE CASES, ASSUMPTIONS, CONSTRAINTS)
        # WORK THROUGH AN EXAMPLE
        # BRAINSTORM SOLUTION
        # IMPLEMENT SOLUTION
        # DEBUG
        # IMPROVE

        # TIME COMPLEXITY: O(LOG N)
        # SPACE COMPLEXITY: 

        # GOAL SHOULD BE TO FIND THE MINIMUM ELEMENT
        # IF THEY WERE ALL THE SAME NUMBER, I WOULD JUST RETURN THAT NUMBER

        left = 0
        right = len(nums) - 1

        while left < right:
            midpoint = (right + left) // 2

            if nums[midpoint] > nums[right]:
                left = midpoint + 1
            
            else:
                right = midpoint

        return nums[left]




