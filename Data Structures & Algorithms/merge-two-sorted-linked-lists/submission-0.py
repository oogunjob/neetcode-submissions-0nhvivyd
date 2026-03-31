# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # RAWBIDI
        # REPEAT THE QUESTION
        # ASK CLARIFICATION
        # WORK THROUGH AN EXAMPLE
        # BRAINSTORM SOLUTION
        # ASK FOR GO AHEAD
        # IMPLEMENT SOLUTION
        # DEBUG
        # IMPROVE
    
        # TIME COMPLEXITY: O(N) BECAUSE WE NEED TO ITERATE OVER THE ENTIRE LISTS
        # SPACE COMPLEXITY: O(N) BECAUSE WE ARE ADDING EVERY ELEMENT TO A NEW LIST

        # NEED TO KEEP A DUMMY NODE
        # 



        dummy = ListNode()
        current = dummy

        l1 = list1
        l2 = list2

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            
            else:
                current.next = l2
                l2 = l2.next
            
            current = current.next

        if l1:
            current.next = l1
        elif l2:
            current.next = l2

        return dummy.next
        