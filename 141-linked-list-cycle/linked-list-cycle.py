# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        n=head
        m=head
        while n is not None and n.next is not None:
            m=m.next
            n=n.next.next
            if m==n:
                return True
    
        return False
            
