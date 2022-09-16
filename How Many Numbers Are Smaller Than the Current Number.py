class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        final=[]
        
        for i in range(len(nums)):
            key=i
            
            count=0
            for j in range(len(nums)):
                if nums[key]>nums[j]:
                    count=count+1
            final.append(count)
            
        return final