# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        curr = slow.next
        slow.next = None
        nextt = None
        prev = None

        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        
        
        temp = head
        while temp and prev:
            tmp1 = temp.next
            tmp2 = prev.next

            prev.next = temp.next
            temp.next = prev

            temp = tmp1
            prev = tmp2
        
        # return head


        

        


        