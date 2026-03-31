class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs:
            output += str(len(string)) + "#" + string

        return output

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            output.append(s[j + 1 :j + 1 + length])
            i = j + 1 + length

        return output




        # RAWBIDI
        # REPEAT THE QUESTION
        # ASK CLARIFICATION (CONSTRAINTS, ASSUMPTIONS, EDGE CASES)
        # WORK THROUGH AN EXAMPLE
        # BRAINSTORM SOLUTION
        # ASK FOR GO AHEAD
        # IMPLEMENT SOLUTION
        # DEBUG
        # IMPROVE

        # TIME COMPLEXITY:
        # SPACE COMPLEXITY:

        # FOR ENCODING IT, LET'S KEEP TRACK OF THE LENGTH OF THE NUMBER AND PUT A DELIMITTER FOR WHEN WE WANT TO DECODE
        # FOR DECODING, FIGURE OUT WHAT THE LENGTH OF THE NUMBER IS
        # GO UP UNTIL THE WORD, APPEND IT TO THE RESULT
        # REPEAT UNTIL THE END OF THE STRING

        # 5$HELLO4$WORLD
