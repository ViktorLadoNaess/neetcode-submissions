# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        curr = dummy
        i =0
        while i <(left-1): 
            curr=curr.next
            i+=1
        if i == 0:
            before = dummy
        else:
            before = curr
        curr= curr.next
        i +=1
        # now time to rearrange
        #print(f'before {before.val} curr {curr.val}')
        prev = None
        end = curr

        while i <=right:
            #print(curr, curr.val)
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr=tmp
            i+=1
        #print(prev.val, curr.val)
        #print(end.val)
        end.next = curr
        before.next = prev

        
        
        return dummy.next
