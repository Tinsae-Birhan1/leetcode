# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        l = []
        while(head.next):
            l.append(head.val)
            head = head.next
        l.append(head.val)
        l.sort()
        head = ListNode(l[0])
        cur = head
        for i in range(1,len(l)):
            head.next = ListNode(l[i])
            head = head.next
        return cur