from linkedlist import *

# Find the middle item in a singly linked list, or two middle items if it contains an even number of nodes.
def get_middle_item(ll):
    fast = ll.head
    slow = ll.head

    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next

    if ll.length() % 2 == 0:
        return slow.data, slow.next.data
    else:
        return slow.data


# Reverse a linked list by reusing the nodes (do not create new nodes).
def reverse_linkedlist(ll):
    prev = None
    current_node = ll.head
    next = None

    while current_node is not None:
        next = current_node.next
        current_node.next = prev
        prev = current_node
        current_node = next

    ll.head = prev

    return ll

if __name__ == "__main__":
    ll = LinkedList(['A','B','C','D'])
    # ll.append('A')
    # ll.append('B')
    # ll.append('C')
    # ll.append('A')
    # ll.append('B')
    # ll.append('C')

    print(get_middle_item(ll))

    print(reverse_linkedlist(ll))
