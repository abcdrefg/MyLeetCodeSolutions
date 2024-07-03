class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverse_list(self, start):
        previous_element = start
        next_element = start.next
        start.next = None
        while next_element:
            head = next_element
            next_element = next_element.next
            head.next = previous_element
            previous_element = head
        return previous_element

    def reverseKGroup(self, head, k: int):
        if k == 1:
            return head
        prev_group_end = head
        current_group_end = head
        current_group_tail = head

        next_node = head.next

        for i in range(1, k):
            head = next_node
            next_node = head.next
            head.next = current_group_tail
            current_group_tail = head
        root = current_group_tail

        if not next_node:
            prev_group_end.next = None
            return root

        while True:
            current_group_end = next_node
            current_group_tail = next_node
            i = 0
            while i < k and next_node:
                head = next_node
                next_node = head.next
                head.next = current_group_tail
                current_group_tail = head
                i += 1
            if not next_node:
                if i < k:
                    current_group_end.next = None
                    current_group_tail = self.reverse_list(current_group_tail)
                    prev_group_end.next = current_group_tail
                    return root
                current_group_end.next = None
                prev_group_end.next = current_group_tail
                return root
            prev_group_end.next = current_group_tail
            prev_group_end = current_group_end
        return root


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

Solution().reverseKGroup(head, 3)