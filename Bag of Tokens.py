class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        l =0 
        r = len(tokens)-1
        while l < r:
            if tokens[l] <= power:
                power -= tokens[l]
                score += 1
                tokens[l] = 0
                l += 1 
            else:
                if score == 0:
                    return 0
                power += tokens[r]
                score -= 1
                r -= 1
        for i in tokens:
            if i!=0 and i<=power:
                power-=i
                score+=1
        return score