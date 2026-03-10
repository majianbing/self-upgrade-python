
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detectCycleStart(head: ListNode) -> ListNode:
    """
    Phase 1: DETECT if cycle exists
    Phase 2: FIND where cycle starts
    """

    if not head or not head.next:
        return None

    # PHASE 1: Detect cycle
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break  # Cycle detected, exit Phase 1
    else:
        return None  # No cycle found

    # PHASE 2: Find cycle start (only runs if cycle detected)
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow  # ✅ The actual cycle start node!

if __name__ == "__main__":
    # Create: 3 → 2 → 0 → -4 → (back to 2)
    node3 = ListNode(3)
    node2 = ListNode(2)
    node0 = ListNode(0)
    node_neg4 = ListNode(-4)

    node3.next = node2
    node2.next = node0
    node0.next = node_neg4
    node_neg4.next = node2  # Cycle!

    result = detectCycleStart(node3)
    assert result == node2  # Should return node 2 ✅
    print(f"Cycle starts at node with value: {result.val}")  # Output: 2