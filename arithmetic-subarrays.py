class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = [None] * len(l)
        
        for i, [start_point, end_point] in enumerate(zip(l, r)):
            s = sorted(nums[start_point:end_point + 1])
            res[i] = all([ s[j] - s[j-1] == s[1] - s[0] for j in range(1, len(s))])
        print(res)
        return res
