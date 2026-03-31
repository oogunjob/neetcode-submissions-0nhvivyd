import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # RAWBIDI
        # REPEAT THE QUESTION
        # ASK CLARIFICATIONM
        # WORK THROUGH AN EXAMPLE
        # BRAINSTORM SOLUTION
        # ASK FOR GO AHEAD
        # IMPLEMENT SOLUTION
        # DEBUG
        # IMPROVE

        # TIME COMPLEXITY: O(LOG N)
        # SPACE COMPLEXITY: O(1)

        # NEED TO COMPUTE THE MIN K -> INITIALIZE IT IS AS MAX(PILES) O(1)
        # BINARY SEARCH BECAUSE WE'RE TRYING TO FIND A VALUE
        # WE'RE GOING TO THEN ITERATE FOR EACH PILE IN THE PILES
        # COMPUTE THE HOURS IT WILL TAKE TO EACH THE BANANAS BASED ON THE MIN K
        # MATH.CEIL(PILE / K)

        min_k = max(piles)
        right = max(piles)
        left = 1
        
        while left <= right:
            k = (right + left) // 2

            # COMPUTE THE HOURS IT WILL TAKE TO EAT EACH BANANAN BASED ON THE K WE'RE TRYING
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)

            if hours <= h:
                min_k = min(min_k, k)
                right = k - 1

            else:
                left = k + 1

        return min_k








            
            
        