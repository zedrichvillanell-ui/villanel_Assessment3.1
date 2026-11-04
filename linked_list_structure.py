class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def main():
    print("=== 2. SINGLY LINKED LIST DATA STRUCTURE ALGORITHM ===")

    head = None
    letters = ['V', 'i', 'l', 'l', 'a', 'n', 'e', 'l']

    print("\n--- Add Phase ---")
    for letter in letters:
        new_node = Node(letter)
        if head is None:
            head = new_node
            print(f"Created head node with data: '{letter}'")
        else:
            current = head
            while current.next is not None:
                current = current.next
            current.next = new_node
            print(f"Appended node with data: '{letter}'")

    # Helper function to display current linked list
    def display_list(current_head):
        elements = []
        curr = current_head
        while curr:
            elements.append(curr.data)
            curr = curr.next
        print(f"Current Linked List: {' -> '.join(elements) if elements else 'Empty'}")

    print()
    display_list(head)

    print("\n--- Remove Phase ---")
    while head is not None:
        temp = head
        head = head.next
        print(f"Deleted node with data: '{temp.data}' (Memory freed)")
        display_list(head)

    # Verify linked list is empty
    if head is None:
        print("\nVerification: Linked List is empty (head == NULL).")


if __name__ == "__main__":
    main()