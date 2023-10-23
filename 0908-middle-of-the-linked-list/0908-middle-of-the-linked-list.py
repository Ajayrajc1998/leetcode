# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def len_of_list(self,head):
        curr=head
        n=0
        while curr:
            n+=1
            curr=curr.next
        return n
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        len_list=self.len_of_list(head)
        if len_list%2==1:
            locate=(len_list+1)//2
        else:
            locate=(len_list//2)+1
        search=0
        curr=head
        result=ListNode()
        res=result
        ans=[]
        flag=False
        while curr:
            if search==locate-1:
                flag=True
            if flag:
                a=ListNode(curr.val)
                result.next=a
                result=result.next
                ans.append(curr.val)
            curr=curr.next
            search+=1
        return res.next