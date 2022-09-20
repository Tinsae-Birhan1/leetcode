# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        
        new = []
        while curr != None:
            h = curr.val
            curr = curr.next
            new.append(h)
            
        new1 = new[::-1]
        sum1 = []
        for i, j in zip(new, new1):
            sum1.append(i+j)
        
        max1 = max(sum1)
        
        return max1