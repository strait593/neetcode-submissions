# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # [2:head, 3:tail]
        curr = head
        prev = None
        placeholder = None

        while curr != None:
            placeholder = curr.next
            curr.next = prev

            prev = curr
            curr = placeholder
            
        return prev