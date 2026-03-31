# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            # DETERMINE THE CURRENT VALUES OF BOTH LISTS
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            # COMPUTE THE VALUE
            val = l1_val + l2_val + carry

            # RESET THE CARRY
            carry = 0

            # DETERMINE WHETHER THERE'S CARRY
            # IF THERE IS, ONLY ADD THE VAL AND KEEP THE CARRY FOR NEXT TIME
            value = 0
            if val > 9:
                value = val % 10
                carry = val // 10
            else:
                value = val

            current.next = ListNode(value)
            current = current.next    
    
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
        