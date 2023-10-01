# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        n=list1
        m=list2
        result=ListNode()
        head=result
        while n and m:
            if n.val>=m.val:
                result.next=ListNode(m.val)
                result=result.next
                m=m.next
            else:
                result.next=ListNode(n.val)
                result=result.next
                n=n.next
        while m:
            result.next=ListNode(m.val)
            result=result.next
            m=m.next
        while n:
            result.next=ListNode(n.val)
            result=result.next
            n=n.next
        head=head.next
        return head