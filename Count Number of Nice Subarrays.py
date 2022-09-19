class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        x = defaultdict(int)
        x[0] = 1
        prefix = 0
        result = 0
        for i in range(len(nums)):
            nums[i] %= 2
        
        for i in nums:
            prefix += i
            if(prefix - k in x):
                result += x[prefix-k]
            x[prefix] += 1
        return result