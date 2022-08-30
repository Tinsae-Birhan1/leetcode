class Solution:
    def numIdenticalPairs(self, nums):
        goodPairs = 0;
        for i in range(len(nums)):
            for j in range(i):
                if (nums[i] == nums[j]):
                    goodPairs += 1
        return goodPairs  
