# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr=head
        res=ListNode()
        result=res
        while curr.next:
            sum_element=0
            temp=curr
            while True:
                sum_element+=temp.val
                temp=temp.next
                if temp.val==0:
                    res.next=ListNode()
                    res.next.val=sum_element
                    res=res.next
                    break
            curr=temp
        return result.next
        