class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)

        l = 0
        result = 0
        mx = Deque()
        mn = Deque()
        mx.append([nums[0], 0])
        mn.append([nums[0], 0])
        for r in range(n):

            while mx and nums[r] > mx[-1][0]:
                mx.pop()
            mx.append([nums[r], r])

            while mn and nums[r] < mn[-1][0]:
                mn.pop()
            mn.append([nums[r], r])

            while l <= r and mx[0][0] - mn[0][0] > limit:
                l += 1

                while mx and l > mx[0][1]:
                    mx.popleft()

                while mn and l > mn[0][1]:
                    mn.popleft()

            result = max(result, r - l + 1)

        return result