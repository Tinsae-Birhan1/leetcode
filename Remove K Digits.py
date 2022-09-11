class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        solution = ""
        n = len(num)
        for item in range(n):
            while solution and k > 0 and solution[-1] > num[item]:
                k -= 1
                solution = solution[:-1]
            solution += num[item]
            if solution == "0":
                solution = ""
        if k > 0:
            if len(solution) >= k:
                solution = solution[0:-k]
            else:
                solution = ""
        if not solution:
            solution = "0"
        return solution