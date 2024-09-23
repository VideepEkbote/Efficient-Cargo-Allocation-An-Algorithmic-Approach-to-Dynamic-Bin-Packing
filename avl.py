#from node import Node

def bincapacityandidcomparator(node1, node2):
    if node1.capacity < node2.capacity or (node1.capacity == node2.capacity and node1.id < node2.id):
        return 0
    elif node1.capacity > node2.capacity or (node1.capacity == node2.capacity and node1.id > node2.id):
        return 1
    else:
        return 2

class AVLTree:
    def __init__(self, compare_function):
        self.root = None
        self.comparator = compare_function

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def getbal(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T2 = y.right

        y.right = z
        z.left = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insert(self,item,node):
        if node is None: return item
        h = self.comparator(item,node)
        if h  == 0: node.left = self.insert(item,node.left)
        elif h == 1: node.right= self.insert(item,node.right)

        node.height = 1 + max(self.height(node.left),self.height(node.right))
        balancefactor = self.getbal(node)

        if balancefactor > 1 and self.comparator(item,node.left) == 0:
            return self.right_rotate(node)

        if balancefactor< -1 and self.comparator(item,node.right) == 1:
            return self.left_rotate(node)

        if balancefactor > 1 and self.comparator(item,node.left) == 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if balancefactor < -1 and self.comparator(item,node.right) == 1:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def inordersucc(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, item, node):
        if node is None:
            return node, None

        if self.comparator(item,node) == 0:
            node.left, deleted = self.delete(item, node.left)
        elif self.comparator(item,node) == 1:
            node.right, deleted= self.delete(item, node.right)
        else:
            deleted = node
            if node.left is None:
                return node.right , deleted
            elif node.right is None:
                return node.left , deleted

            temp = self.inordersucc(node.right)
            node.capacity, node.id = temp.capacity, temp.id  # Swap the inorder successor's values
            node.right, waste = self.delete(temp, node.right)

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.getbal(node)

        if balance > 1 and self.getbal(node.left) >= 0:
            return self.right_rotate(node), deleted
        if balance < -1 and self.getbal(node.right) <= 0:
            return self.left_rotate(node), deleted
        if balance > 1 and self.getbal(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node), deleted
        if balance < -1 and self.getbal(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node), deleted

        return node, deleted

    def remove(self, item):
        self.root, deleted= self.delete(item, self.root)
        return deleted


# Node class (for your implementation)
class Node:
    def __init__(self, capacity, id):
        self.capacity = capacity
        self.id = id
        self.left = None
        self.right = None
        self.height = 1  # height initialized as 1 for the new node


# Function to print the in-order traversal of the AVL tree
def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        print(f"[Capacity: {node.capacity}, Bin ID: {node.id}, Height: {node.height}]")
        in_order_traversal(node.right)


# Function to check the balance factors of each node
def check_balances(node, tree):
    if node is None:
        return True

    left_balanced = check_balances(node.left, tree)
    right_balanced = check_balances(node.right, tree)

    balance_factor = tree.getbal(node)
    if abs(balance_factor) > 1:
        print(
            f"Unbalanced at Node [Capacity: {node.capacity}, Bin ID: {node.id}] with balance factor: {balance_factor}")
        return False
    return left_balanced and right_balanced


# Create the AVL tree and insert nodes based on examples
def run_tests():
    avl = AVLTree(bincapacityandidcomparator)

    # Example 1: Simple Insertions
    nodes_to_insert = [
        Node(50, 1),
        Node(30, 2),
        Node(70, 3),
        Node(20, 4),
        Node(40, 5),
        Node(60, 6),
        Node(80, 7)
    ]
    print("Inserting nodes into the AVL tree:")
    for node in nodes_to_insert:
        avl.root = avl.insert(node, avl.root)

    print("\nIn-Order Traversal after insertions:")
    in_order_traversal(avl.root)

    # Check if the tree is balanced
    print("\nChecking balance of each node:")
    is_balanced = check_balances(avl.root, avl)
    if is_balanced:
        print("Tree is balanced after insertions.\n")
    else:
        print("Tree is not balanced after insertions.\n")

    # Example 2: Deletion
    print("Deleting node with [Capacity: 50, Bin ID: 1]")
    avl.remove(Node(50, 1))

    print("\nIn-Order Traversal after deletion:")
    in_order_traversal(avl.root)

    # Check if the tree is balanced
    print("\nChecking balance of each node after deletion:")
    is_balanced = check_balances(avl.root, avl)
    if is_balanced:
        print("Tree is balanced after deletion.\n")
    else:
        print("Tree is not balanced after deletion.\n")

    # Example 3: Insertion with same capacity, different IDs
    avl = AVLTree(bincapacityandidcomparator)  # Reset the tree
    nodes_to_insert_same_capacity = [
        Node(50, 1),
        Node(50, 2),
        Node(30, 5),
        Node(50, 3),
        Node(30, 4),
        Node(30,3)

    ]
    print("Inserting nodes with same capacity into the AVL tree:")
    for node in nodes_to_insert_same_capacity:
        avl.root = avl.insert(node, avl.root)

    print("\nIn-Order Traversal after same capacity insertions:")
    in_order_traversal(avl.root)

    # Check if the tree is balanced
    print("\nChecking balance of each node after same capacity insertions:")
    is_balanced = check_balances(avl.root, avl)
    if is_balanced:
        print("Tree is balanced after same capacity insertions.\n")
    else:
        print("Tree is not balanced after same capacity insertions.\n")

    # Example 4: Deleting a node
    print("Deleting node with [Capacity: 50, Bin ID: 1]")
    avl.remove(Node(50, 1))

    print("\nIn-Order Traversal after deletion:")
    in_order_traversal(avl.root)

    # Check if the tree is balanced
    print("\nChecking balance of each node after deletion:")
    is_balanced = check_balances(avl.root, avl)
    if is_balanced:
        print("Tree is balanced after deletion.\n")
    else:
        print("Tree is not balanced after deletion.\n")


# Run the tests
run_tests()
