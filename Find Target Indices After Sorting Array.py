class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        final=[]
        for i in range(len(nums)):
            for j in range(0, len(nums)-1-i):
                if nums[j+1]< nums[j]:
                    temp=nums[j+1]
                    nums[j+1]=nums[j]
                    nums[j]=temp
        for k in range(len(nums)):
            if nums[k]==target:
                final.append(k)
        return final