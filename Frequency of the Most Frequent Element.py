class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        r,l=0,0
        total, output=0, 0
        while r< len(nums):
            total+=nums[r]
           
            while nums[r]*(r-l+1)> total+k:
                total-=nums[l]
                l+=1
            output=max (output, r-l+1)
            r+=1
        return output
            