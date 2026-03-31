class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = { ")": "(", "}": "{", "]": "[" }
        stack = []

        for paren in s:
            if paren in hashmap:
                if stack and stack[-1] == hashmap[paren]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(paren) 

        return True if not stack else False
        