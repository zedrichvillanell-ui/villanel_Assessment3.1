class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# Preorder Traversal: Root -> Left -> Right
def print_preorder(node):
    if node is None:
        return
    print(node.val, end=" ")
    print_preorder(node.left)
    print_preorder(node.right)


# Inorder Traversal: Left -> Root -> Right
def print_inorder(node):
    if node is None:
        return
    print_inorder(node.left)
    print(node.val, end=" ")
    print_inorder(node.right)


# Postorder Traversal: Left -> Right -> Root
def print_postorder(node):
    if node is None:
        return
    print_postorder(node.left)
    print_postorder(node.right)
    print(node.val, end=" ")


if __name__ == "__main__":
    # Constructing the Binary Tree based on Assessment 3.5
    root = Node('Z')

    # Level 1
    root.left = Node('E')
    root.right = Node('D')

    # Level 2
    root.left.left = Node('R')
    root.left.right = Node('I')
    root.right.left = Node('C')
    root.right.right = Node('H')

    # Level 3 (Leaves matching "VILLANEL")
    root.left.left.left = Node('V')

    root.left.right.left = Node('I')
    root.left.right.right = Node('L')

    root.right.left.left = Node('L')
    root.right.left.right = Node('A')

    root.right.right.left = Node('N')
    root.right.right.right = Node('E')

    print("=== Assessment 3.6: DFS Tree Traversals ===")

    print("Preorder Traversal:  ", end="")
    print_preorder(root)
    print()

    print("Inorder Traversal:   ", end="")
    print_inorder(root)
    print()

    print("Postorder Traversal: ", end="")
    print_postorder(root)
    print()