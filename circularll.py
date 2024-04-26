class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def remove(self, key):
        if self.head is None:
            print("List is empty")
            return

        # Case 1: Only one node is present
        if self.head.data == key and self.head.next == self.head:
            self.head = None
            return

        # Case 2: Removing head node
        if self.head.data == key:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            return

        # Case 3: Removing node other than head
        prev = None
        current = self.head
        while current.next != self.head:
            prev = current
            current = current.next
            if current.data == key:
                prev.next = current.next
                return
        print(f"Node with data {key} not found")

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("head")


# Main program
linked_list = CircularLinkedList()

while True:
    print("\n1. Add node")
    print("2. Remove node")
    print("3. Display the list")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        data = input("Enter data to add: ")
        linked_list.add(data)
    elif choice == '2':
        key = input("Enter data of node to remove: ")
        linked_list.remove(key)
    elif choice == '3':
        linked_list.display()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
