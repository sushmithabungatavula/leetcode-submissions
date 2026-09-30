# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # vals=[]
        # curr=head
        # while curr:
        #     vals.append(curr)
        #     curr=curr.next
        # left=0
        # right=len(vals)-1
        # while left<right:
        #     vals[left].next=vals[right]
        #     left+=1
        #     if left==right:
        #         break
        #     vals[right].next=vals[left]
        #     right-=1
        # vals[left].next=None


        
        #first find mid -- use 2 pointers slow and fast
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        #if fast.next=None then slow is mid and slow.next = new list head
        #then rev second half
        second=slow.next
        prev=None
        slow.next=None
        while second:
            #save next pointer first, then rever the pointers
            temp=second.next
            second.next=prev
            prev=second
            second=temp #return prev as its head of second list
        #merge two lists
        first=head
        second=prev
        while second:
            temp1=first.next
            temp2=second.next
            first.next=second
            second.next=temp1
            first=temp1
            second=temp2


        





        