class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        cur = len(cardPoints)-k
        
        current = sum(cardPoints[cur:])
        index = 0
        ans = current
        while cur<len(cardPoints):
            current = current - cardPoints[cur] + cardPoints[index]
            ans = max(ans, current)
            cur+=1
            index+=1
        return ans