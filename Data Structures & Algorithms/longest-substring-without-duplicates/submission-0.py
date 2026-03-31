class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # two pointer
        # need to keep a seen array 
        maximum = 0
        seen = set()
        left = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            maximum = max(maximum, right - left + 1)
            seen.add(s[right])

        return maximum
        