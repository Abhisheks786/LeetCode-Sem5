# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return False

        fast=head
        slow=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

            

        sec=slow.next
        slow.next=None
        prev=None
        while sec:
            tmp = sec.next
            sec.next = prev
            prev = sec
            sec = tmp

        first=head
        sec=prev

        while first and sec:
            temp1, temp2 = first.next, sec.next
            first.next = sec
            sec.next=temp1
            first=temp1
            sec=temp2
        




