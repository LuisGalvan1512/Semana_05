from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = deque()
    queue.append(root)

    while queue:
        current = queue.popleft()
        result.append(current.value)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result

# Tests

# Constructing the tree:
#       A
#      / \
#     B   C
#    / \   \
#   D   E   F

root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")
root.left.left = TreeNode("D")
root.left.right = TreeNode("E")
root.right.right = TreeNode("F")

print(level_order_traversal(root))  
# Expected output: ['A', 'B', 'C', 'D', 'E', 'F']

