# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
        def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
            x = 0
            current = head
            while current:
                x+=1
                current = current.next

            
            item = 0
            while(item<x//2):
                head = head.next
                item+=1
            return head
	