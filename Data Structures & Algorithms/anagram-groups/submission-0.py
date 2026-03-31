from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # RAWBIDI
        # REPEAT THE QUESTION
        # ASK CLARIFICATION (CONSTRAINTS, ASSUMPTIONS, EDGE CASES)
        # WORK THROUGH AN EXAMPLE
        # BRAINSTORM SOLLUTION
        # ASK FOR GO AHEAD
        # IMPLEMENT SOLUTION
        # DEBUG
        # IMPROVE

        # PATTERN:

        # TIME COMPLEXITY:
        # SPACE COMPLEXITY:

        # CREATE A HASHAMP => {[(a, 1), (c, 1), (t, 1)]: []} 
        # CHECK EACH STRING IN THE STRS LIST AND ADD THEM ACCORDINGLY
        # RETURN THE VALUES FROM THE HASHMAP

        # declare the output dictionary
        output = defaultdict(list)

        for string in strs:
            # determine what the key will look like
            # ex: [(a, 1), (c, 1), (t, 1)]
            key = "".join(sorted(string))

            output[key].append(string)
        

        return list(output.values())
