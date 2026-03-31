class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # RAWBIDI
        # REPEAT THE QUESTION
        # ASK CLARIFICATION
        # WORK THROUGH AN EXAMPLE
        # BRAINSTORM SOLUTION
        # ASK FOR GO AHEAD
        # IMPLEMENT SOLUTION
        # DEBUG
        # IMPROVE

        # TIME COMPLEXITY: O(LOG N)
        # SPACE COMPLEXITY: O(1)

        # WE NEED TO FIND THE SMALLEST ELEMENT IN THE ARRAY, THIS WILL GIVE US THE MIN INDEX

        # NEED TO DETERMINE WHICH SIDE THE TARGET IS IN
        # BASE CASE
        # LEFT PARTITION
        # RIGHT PARTITION

        # SEARCH FOR THE ELEMENT

        left = 0
        right = len(nums) - 1

        while left < right:
            midpoint = (right + left) // 2

            if nums[midpoint] > nums[right]:
                left = midpoint + 1
            else:
                right = midpoint

        min_index = left

        if min_index == 0:
            left = 0
            right = len(nums) - 1
        elif target >= nums[0] and target <= nums[min_index - 1]:
            left = 0
            right = min_index - 1
        else:
            left = min_index
            right = len(nums) - 1

        while left <= right:
            midpoint = (right + left) // 2

            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                left = midpoint + 1
            else:
                right = midpoint - 1

        return -1
        