from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

def dfs_preorder(root):
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

if __name__ == "__main__":
    # Constructing Binary Tree from diagram
    root = TreeNode('V')
    root.left = TreeNode('I')
    root.right = TreeNode('L')
    root.left.left = TreeNode('L')
    root.left.right = TreeNode('A')
    root.right.left = TreeNode('N')
    root.right.right = TreeNode('E')
    root.left.left.left = TreeNode('L')

    print("Binary Tree BFS Traversal:", " -> ".join(bfs(root)))
    print("Binary Tree DFS Traversal:", " -> ".join(dfs_preorder(root)))