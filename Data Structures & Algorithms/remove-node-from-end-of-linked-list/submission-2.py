# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = r = head
        gap = 0
        while r:
            if gap > n:
                l = l.next
            r = r.next
            gap += 1
        print(l.val)
        if l.next and gap != n:
            print("exec")
            l.next = l.next.next
        else: head = l.next
        return head

