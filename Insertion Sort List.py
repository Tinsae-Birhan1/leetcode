# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=-50001, next=head)
        prev = dummy
        curr = head
        while curr:
            
            if curr.val < prev.val:
                
                prev.next = curr.next
                
                
                start = dummy
                while start.next.val < curr.val:
                    start = start.next
                    
                curr.next = start.next
                start.next = curr
                
                curr = prev
                
            prev = curr
            curr = curr.next
        
        return dummy.next