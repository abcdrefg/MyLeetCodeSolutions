class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def addArray(self, linkedList, head):
        while True:
            if not linkedList:
                return head
            head.next = ListNode(linkedList.val)
            linkedList = linkedList.next
            head = head.next

    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            head = ListNode(list1.val)
            list1 = list1.next
        else:
            head = ListNode(list2.val)
            list2 = list2.next
        root = head
        while True:
            if not list1:
                self.addArray(list2, head)
                break
            if not list2:
                self.addArray(list1, head)
                break
            if list1.val < list2.val:
                head.next = ListNode(list1.val)
                head = head.next
                list1 = list1.next
            else:
                head.next = ListNode(list2.val)
                head = head.next
                list2 = list2.next
        return root