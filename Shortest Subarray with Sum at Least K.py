class Solution:
    import collections
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sum=[0]
        
        
        for i in range(n):
            sum.append(nums[i]+sum[-1])
        x = collections.deque()
        ans = n+1
        for idx,s in enumerate(sum):
            while x and s-sum[x[0]] >=k:
                ans = min(ans,idx -x.popleft() )
            while x and s <= sum[x[-1]]:
                x.pop()
            x.append(idx)
        return ans if ans < n+1 else -1
            