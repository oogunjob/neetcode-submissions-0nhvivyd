class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # RAWBIDI
        # REPEAT THE QUESTION
        # ASK CLARIFICATION
        # WORK THROUGH AN EXAMPLE
        # BRAINSTORM SOLUTION
        # ASK FOR GO AHEAD
        # IMPLEMENT SOLUTION
        # DEBUG
        # IMPROVE

        # SPACE COMPLEXITY: O(N)
        # TIME COMPLEXITY: O(N)

        stack = []

        for token in tokens:
            # Check if the token is an operation
            if token in ("+", "-", "/", "*"):
                num = stack.pop()
                
                if token == "+":
                    stack[-1] += num

                elif token == "-":
                    stack[-1] -= num

                elif token == "*":
                    stack[-1] *= num

                else:
                    stack[-1] = int(stack[-1] / num)

            else:
                stack.append(int(token))

        return stack[-1]