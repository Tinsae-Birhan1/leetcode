# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        container = []
        pos = -1
        
        stack = []
        
        while head:
            
            container.append(0)
            pos += 1
            
            while stack and stack[-1][1] < head.val:
                Y, curr = stack.pop()
                container[Y] = head.val
            
            
            stack.append((pos, head.val))
            head = head.next
        
        return container