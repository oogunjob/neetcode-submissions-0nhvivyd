class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # RAWBIDI
        # REPEAT THE QUESTION
        # ASK CLARIFICATION
        # WORK THROUGH AN EXAMPLE
        # BRAINSTORM SOLUTION
        # ASK FOR GO AHEAD
        # IMPLEMENT SOLUTION
        # DEBUG
        # IMPROVE

        # TIME COMPLEXITY: O(N)
        # SPACE COMPLEXITY: O(1)

        # ITERATE THROUGH THE ARRAY
        # KEEP TRACK OF THE PROFIT
        # KEEP TRACK OF THE LEAST PRICE

        max_profit = 0
        min_price = float("inf")
        
        for price in prices:
            profit = price - min_price
            max_profit = max(max_profit, profit)
            min_price = min(price, min_price)

        return max_profit
        