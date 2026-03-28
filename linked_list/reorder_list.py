"""
Problem: Reorder List (LC 143 — Medium)
Given the head of a singly linked list:
L0 → L1 → L2 → ... → Ln-1 → Ln
Reorder it to:
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...
You may not modify the values in the nodes — only the node connections.
Example 1:
Input:  1 → 2 → 3 → 4
Output: 1 → 4 → 2 → 3
Example 2:
Input:  1 → 2 → 3 → 4 → 5
Output: 1 → 5 → 2 → 4 → 3
"""


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


def reorder(head):
    temp_list = []
    while head:
        temp_list.append(head)
        head = head.next
    left = 0
    right = len(temp_list) - 1
    print(temp_list, left, right)
    while left < right:
        temp_list[left].next = temp_list[right]
        temp_list[right].next = temp_list[left + 1]
        left += 1
        right -= 1
    # left cross first.
    temp_list[left].next = None


def to_list(head):
    """Helper: convert linked list to Python list for easy printing"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    print("reorder list ")
    # Test 1: odd length
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    reorder(head)
    print(to_list(head))  # Expected: [1, 5, 2, 4, 3]

    # Test 2: even length
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    reorder(head)
    print(to_list(head))  # Expected: [1, 4, 2, 3]

    # Test 3: single node
    head = ListNode(1)
    reorder(head)
    print(to_list(head))  # Expected: [1]

    # Test 4: two nodes
    head = ListNode(1, ListNode(2))
    reorder(head)
    print(to_list(head))  # Expected: [1, 2]
