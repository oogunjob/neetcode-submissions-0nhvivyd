from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)
        for string in strs:
            key = "".join(sorted(string))
            dictionary[key].append(string)

        return [value for key, value in dictionary.items()]
            
        