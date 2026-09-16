# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        uniques = set()
        
        while cur:
            if cur in uniques:
                return True
            uniques.add(cur)
            cur = cur.next
        
        return False