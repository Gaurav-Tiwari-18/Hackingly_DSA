# Q-Write a program to remove duplicates from an unsorted linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def remove_duplicates(self):
        current = self.head
        prev = None
        seen = set()
        while current:
            if current.data in seen:
                prev.next = current.next
            else:
                seen.add(current.data)
                prev = current
            current = current.next

    def to_list(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

# Example usage:
ll = LinkedList()
input_data = [3, 5, 3, 7, 8, 5, 10]
for item in input_data:
    ll.append(item)

print("Original list:", ll.to_list())
ll.remove_duplicates()
print("List after removing duplicates:", ll.to_list())
