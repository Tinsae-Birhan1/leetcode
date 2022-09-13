class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        item= 1 
        s='0'
        hash_map ={'1': '0', '0': '1'}
        for item in range(1, n):
            s = s + '1' + ''.join((hash_map[item] for item in s))[::-1]
        return s[k-1]