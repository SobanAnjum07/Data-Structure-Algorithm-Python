class Node:
    """
    A node in a doubly linked list.
    """
    def __init__(self, data=None):
        self.data = data
        self.prev = None  # Reference to the previous node
        self.next = None  # Reference to the next node


class DoublyLinkedList:
    """
    Doubly linked list implementation.
    """
    def __init__(self):
        self.head = None  # Reference to the first node in the list

    def is_empty(self):
        """
        Check if the doubly linked list is empty.
        """
        return self.head is None

    def insert_at_beginning(self, data):
        """
        Insert a new node at the beginning of the list.
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        """
        Insert a new node at the end of the list.
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete(self, data):
        """
        Delete a node with the given data from the list.
        """
        if self.is_empty():
            return
        
        # If the node to delete is the head node
        if self.head.data == data:
            if self.head.next is not None:
                self.head.next.prev = None
            self.head = self.head.next
            return

        current = self.head
        while current is not None:
            if current.data == data:
                # If the node to delete is not the last node
                if current.next is not None:
                    current.next.prev = current.prev
                current.prev.next = current.next
                return
            current = current.next

    def display(self):
        """
        Display the elements of the doubly linked list.
        """
        if self.is_empty():
            print("Doubly linked list is empty.")
        else:
            current = self.head
            while current is not None:
                print(current.data, end=" ")
                current = current.next
            print()
