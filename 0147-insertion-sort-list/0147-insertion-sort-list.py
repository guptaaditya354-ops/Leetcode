# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
       # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to act as the head of the sorted list
        dummy = ListNode(0)
        curr = head
        
        while curr:
            # At each step, remember the next node to process
            next_node = curr.next
            
            # Find the position to insert 'curr' in the sorted list
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
                
            # Insert curr between prev and prev.next
            curr.next = prev.next
            prev.next = curr
            
            # Move to the next node in the original unsorted list
            curr = next_node
            
        return dummy.next