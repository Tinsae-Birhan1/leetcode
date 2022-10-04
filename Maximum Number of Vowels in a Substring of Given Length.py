class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        v = 0
        for i in range(k):
            if s[i] in "aeiou":
                v += 1
        result = v
        for i in range(len(s) - k):
            if s[i] in "aeiou":
                v -= 1
            if s[i + k] in "aeiou":
                v += 1
            result = max(result, v)
        return result