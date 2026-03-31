class Solution:
    def isPalindrome(self, s: str) -> bool:
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

        # my idea is to create a new string with the letters in lowercase and only check for letters

        t = ""
        for char in s:
            if char.isalpha() or char.isdigit():
                t += char.lower()

        return t == t[::-1]
        