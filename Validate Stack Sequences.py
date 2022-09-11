class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        stack = []
        x = 0
        for item in range(n):
            stack.append(pushed[item])
            while stack and x < n and stack[-1] == popped[x]:
                stack.pop()
                x += 1
        return not stack