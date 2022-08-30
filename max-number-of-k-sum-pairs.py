class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hash = defaultdict(int)
        var = 0 
        
        for x in nums:
            target = k - x
            
            if hash[target] > 0:
                hash[target] -= 1
                var += 1
            else:
                hash[x] += 1
                
        return var
        
