"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.next is not None:
            self.next.prev = self.prev

        if self.prev is not None:
            self.prev.next = self.next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        new_node = ListNode(value)
        if len(self) == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        value = self.head.value
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head.delete()
            self.head = self.head.next

        self.length -= 1
        return value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value)
        if len(self) == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        value = self.tail.value
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.tail.delete()
            self.tail = self.tail.prev

        self.length -= 1
        return value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if self.head.next is not None and node is not self.head:
            if node is self.tail:
                self.tail = self.tail.prev
            node.delete()
            self.length -= 1
            self.add_to_head(node.value)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if self.head.next is not None and node is not self.tail:
            if node is self.head:
                self.head = self.head.next
            node.delete()
            self.length -= 1
            self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        if self.head.next is None:
            self.head = None
            self.tail = None
        elif node is self.head:
            node.delete()
            self.head = node.next
        elif node is self.tail:
            node.delete()
            self.tail = node.prev

        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        current = self.head.next
        max_val = self.head.value
        while current is not None:
            if current.value > max_val:
                max_val = current.value
            current = current.next

        return max_val
