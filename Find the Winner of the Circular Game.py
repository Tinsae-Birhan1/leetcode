class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        container = [item for item in range(1,n+1)]
        item =0
        while len(container) > 1 :
            n = len(container)
            item = (item+k-1) % n
            container.pop(item)
                   
            
            
            
        return container[0]
            