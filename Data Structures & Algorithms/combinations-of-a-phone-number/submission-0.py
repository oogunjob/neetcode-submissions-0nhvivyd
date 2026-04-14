class Solution:
    def letterCombinations(self, digits: str) -> List[str]:



        # this is a backtracking problem
        # 

        # need to create a backtracking function
        # because it's a decision tree
        # base case 
        # need to store the result in an array
        # i == len(digits)

        # pass in the index
        # recurse through the hashmap with the digits
        res = []

        hashmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i, currentStr):
            if i == len(digits):
                res.append(currentStr)
                return

            for c in hashmap[digits[i]]:
                backtrack(i + 1, currentStr + c)

        if digits:
            backtrack(0, "")

        return res
        