# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        result=""
        
        while head.next:
            result+=(str(head.val))
            
            head = head.next
            
        result+= str(head.val)
        
        return result== result[::-1]  