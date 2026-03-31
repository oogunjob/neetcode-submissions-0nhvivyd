class Solution:
    def findMin(self, nums: List[int]) -> int:
        # RAWBIDI
        # REPEAT THE QUESTION
        # ASK CLARIFICATION
        # WORK THROUGH AN EXAMPLE
        # BRAINSTORM SOLUTION
        # ASK FOR GO AHEAD
        # IMPLEMENT SOLUTION
        # DEBUG
        # IMPROVE

        # [3,4,5,6,1,2]
        #  L   M     R

        left = 0
        right = len(nums) - 1

        while left < right:
            midpoint = (right + left) // 2
            if nums[midpoint] > nums[right]:
                left = midpoint + 1

            else:
                right = midpoint

        return nums[left]
        