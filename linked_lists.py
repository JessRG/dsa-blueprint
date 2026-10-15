# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, values: list):
        if len(values) == 0:
            self.head = None
            return

        self.head = ListNode(values[0])
        curr = self.head
        for val in values[1:]:
            curr.next = ListNode(val)
            curr = curr.next

    def __str__(self):
        return LinkedList.stringify(self.head)

    @staticmethod
    def stringify(head: ListNode) -> str:
        curr = head
        list = []
        while curr:
            list.append(curr.val)
            curr = curr.next
        return str(list)

    @staticmethod
    def visualize(head: ListNode) -> str:
        curr = head
        nodes = []
        while curr:
            nodes.append(str(curr.val))
            curr = curr.next
        nodes.append("None")
        return " -> ".join(nodes)

# Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.
#
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#
# Example 2:
# Input: head = [1,2]
# Output: [2,1]
#
# Example 3:
# Input: head = []
# Output: []
#
# Constraints:
# The number of nodes in the list is the range[0, 5000].
# -5000 <= Node.val <= 5000
# Follow up: A linked list can be reversed either iteratively or recursively.Could you implement both?
def reverseList(head: ListNode | None) -> ListNode | None:
    if not head:
        return head

    prev = None
    curr = head
    next = curr.next
    while curr:
        curr.next = prev
        prev = curr
        curr = next

        if curr:
            next = curr.next

    head = prev
    return head
values = [1,2,3,4,5]
linked_list = LinkedList(values)
head = reverseList(linked_list.head)
print(LinkedList.stringify(head))
print(LinkedList.visualize(head))