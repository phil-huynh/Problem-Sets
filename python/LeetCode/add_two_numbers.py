

def sum_col(v1, v2, carried):
    total = v1 + v2 + carried
    result = total if total < 10 else int(str(total)[-1])
    carry = 0 if total < 10 else 1
    return result, carry

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        final = ListNode()
        node, carried = final, 0

        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            node.val, carried = sum_col(num1, num2, carried)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if l1 or l2:
                node.next = ListNode()
                node = node.next
            else:
                node.next = ListNode() if carried else None
        return final

