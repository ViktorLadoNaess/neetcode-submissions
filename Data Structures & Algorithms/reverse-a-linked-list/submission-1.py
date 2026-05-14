# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        curr = head

        while curr != None:
            nxt = curr.next #store nxt value
            curr.next = prev # set curr nex to point to prev
            prev = curr # update prev
            curr = nxt
        return prev

