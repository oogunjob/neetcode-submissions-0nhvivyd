class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # RAWBIDI
        # REPEAT THE QUESTION
        # ASK CLARIFICATION
        # WORK THROUGH AN EXAMPLE
        # BRAINSTORM SOLUTION
        # ASK FOR GO AHEAD
        # IMPLEMENT SOLUTION
        # DEBUG
        # IMRPOVE

        # TIME COMPLEXITY: O(N)
        # SPACE COMPLEXITY: O(1) # the output array

        # KEEP A POINTER ON EACH END AND SEE IF THE ADD UP TO THE NUMBER
        # IF THE SUM IS TOO LARGE, THEN MOVE THE RIGHT POINTER TO THE LEFT
        # IF THE SUM IS TOO SMALL, THEN MOVE THE LEFT POINTER TO THE RIGHT

        left = 0
        right = len(numbers) - 1

        while left < right:
            summ = numbers[left] + numbers[right]

            # Check if the sum is equal to the target, if so, return the answer
            if summ == target:
                return [left + 1, right + 1]

            # Check if the sum is less than the target, if so, increment left pointer
            elif summ < target:
                left += 1

            # If the sum is greater than target, reduce right pointer
            else:
                right -= 1

        return []