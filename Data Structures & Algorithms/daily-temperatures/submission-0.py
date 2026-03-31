class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # RAWBIDI
        # REPEAT THE QUESTION
        # ASK CLARIFICATION
        # WORK THROUGH AN EXAMPLE
        # BRAINSTORM SOLUTION
        # ASK FOR GO AHEAD
        # IMPLEMENT SOLUTION
        # DEBUG
        # IMPROVE

        # TIME COMPLEXITY:
        # SPACE COMPLEXITY:

        # INITIALIZE A RESULT ARRAY THAT ALL STARTS WITH 0
        # I NEED TO ENUMERATE OVER THE TEMPS
        # WHILE 

        result = [0] * len(temperatures)
        stack = [] # temperature, i

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                index = stack[-1][1]
                result[index] = i - stack[-1][1]
                stack.pop()

            stack.append((temp, i))
        
        return result