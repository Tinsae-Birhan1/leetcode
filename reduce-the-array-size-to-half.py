class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        m = {}
        for i in arr:
            if i not in m:
                m[i]  = 1
            else:
                m[i] += 1
                
        h = sorted(m.values())
        length = len(arr)//2
        ans = 0
        
        while length > 0:
            length -= h.pop()
            ans += 1
        return ans
