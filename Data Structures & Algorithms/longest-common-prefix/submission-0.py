class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:


        # sort them


        # need to compare the first one with the last one


        strs.sort()
        i = 0
        res = ""

        while i < len(strs[0]) and i < len(strs[-1]):
            if strs[0][i] != strs[-1][i]:
                break

            res += strs[0][i]
            i += 1

        return res
        