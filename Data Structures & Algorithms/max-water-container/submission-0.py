class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # RAWBIDI
        # REPEAT THE QUESTION
        # ASK CLARIFICATION (CONSTRAINTS, EDGE CASES, ASSUMPTIONS)
        # WORK THROUGH AN EXAMPLE
        # BRAINSTORM SOLUTION
        # ASK FOR GO AHEAD
        # IMPLEMENT SOLUTION
        # DEBUG
        # IMPROVE

        # TIME COMPLEXITY:
        # SPACE COMPLEXITY:

        # PATTERN: TWO POINTER

        # USE A TWO POINTER APPROACH
        # KEEP A POINTER ON THE LEFT SIDE AND RIGHT SIDE
        # KEEP TRACK OF A MAX_AREA VARIABLE
        # EVERY TIME WE ENCOUNTER AN AREA, COMPARE AGAINST IT AND UPDATE WHERE NECESSARY
        # COMPUTE THE AREA BY USING THE MIN HEIGHT THAT WE ARE ON
        # IF THE HEIGHT OF LEFT IS LESS THAN HEIGHT OF RIGHT, MOVE LEFT TO THE RIGHT
        # VICE VERSE FOR RIGHT SIDE

        max_area = 0
        left = 0
        right = len(heights) - 1

        while left <= right:
            # compute the area and compare against the max_area
            area = min(heights[left], heights[right]) * (right - left)
            max_area = max(max_area, area)

            if heights[left] < heights[right]:
                left += 1

            else:
                right -= 1

        return max_area






        