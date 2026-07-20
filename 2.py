# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ''
        num2 = ''
        while True:
            num1 += str(l1.val)
            if l1.next == None:
                break
            l1 = l1.next
        while True:
            num2 += str(l2.val)
            if l2.next == None:
                break
            l2 = l2.next
        num1 = num1[::-1]
        num2 = num2[::-1]
        final = int(num1) + int(num2)
        final = list(str(final)[::-1])
        n1 = ListNode(int(final[0]),None)
        prev = n1
        for i in range(1,len(final)):
            prev.next = ListNode(int(final[i]),None)
            prev = prev.next
        return n1