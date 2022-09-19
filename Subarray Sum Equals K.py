class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum=0
        
        for i in range(len(nums)):
            prefixSums = Counter()
            prefixSums[0] = 1
            Sum = 0
            result = 0
            for i in range(len(nums)):
                Sum += nums[i]
                result += prefixSums[Sum - k]
                prefixSums[ Sum] += 1
            return result
            
            
             