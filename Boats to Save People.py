class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat=0
        l=0
        r=len(people)-1
        people.sort()
        while l<=r:
            rem=limit- people[r]
            boat+=1
            r-=1
            if l<=r and rem>=people[l]:
                l+=1
        return boat