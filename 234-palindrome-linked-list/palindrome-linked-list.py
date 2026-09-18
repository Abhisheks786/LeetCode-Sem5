# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:
            return True

        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        prev = None
        curr = slow
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        
        fir, sec = head, prev
        while sec:  
            if fir.val != sec.val:
                return False
            fir = fir.next
            sec = sec.next

        return True