class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        result = set()
        x = 0
        for right in range(len(s)):
            while s[right] in result:
                result.remove(s[left])
                left += 1
            result.add(s[right])
            x = max(x, right - left + 1)
        return x