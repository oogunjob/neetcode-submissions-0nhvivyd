class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # RAWBIDI
        # REPEAT THE QUESTION
        # ASK CLARIFICATION (CONSTRAINTS, EDGE CASES, ASSUMPTIONS)
        # WORK THROUGH AN EXAMPLE
        # BRAINSTORM SOLUTION
        # ASK FOR GO AHEAD
        # IMPLEMENT SOLUTION
        # DEBUG
        # IMPROVE

        # TIME COMPLEXITY: O(log n)
        # SPACE COMPLEXITY:


        # NOTES:        
        # THERE'S A CHANCE THAT ALL OF THE NUMBERS COULD BE POSITIVE
        # IF THAT'S THE CASE THEN IT WOULD BE IMPOSSIBLE TO RETURN AN OUTPUT WITH INDICIES
        # SAME FOR NEGATIVE
        # IF THERE'S NOT AT LEAST 3, RETURN NOTHING

        # [-4, -1, -1, 0, 1, 2]

        nums.sort()
        output = []
    
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                summ = nums[i] + nums[left] + nums[right]

                if summ == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif summ < 0:
                    left += 1

                else:
                    right -= 1



        return output







