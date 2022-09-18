class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:

        l = Counter(changed)
        result=[]
        if len(changed)%2 != 0: 
            return []
        for i in sorted(l.keys()):
            
            if l[i] > l[i*2]: 
                return []
            if i == 0:
                if l[i]%2 != 0: 
                    return []
                result += [i]*(l[i]//2)
            else:
                result+=[i]*l[i]
                l[i*2] -= l[i]
        return result