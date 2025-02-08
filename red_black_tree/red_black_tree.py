import enum

class Color(enum.Enum):
    """Enum class to represent the color of a node in a Red-Black Tree"""
    RED = "R"
    BLACK = "B"

class RedBlackTree:

    class Node:
        def __init__(self, key, color=Color.RED):
            self.key = key
            self.color = color
            self.parent = None
            self.right = None
            self.left = None
        
        def __str__(self):
            return f"{self.key} ({self.color.value})"
        
        def grandparent(self):
            """Returns the grandparent of the node"""
            if self.parent is None:
                return None
            return self.parent.parent
        
        def sibling(self):
            """Returns the sibling of the node"""
            if self.parent is None:
                return None
            if self == self.parent.left:
                return self.parent.right
            return self.parent.left

        def uncle(self):
            """Returns the uncle of the node"""
            if self.parent is None:
                return None
            return self.parent.sibling()

    def __init__(self):
        self.NIL = self.Node(None, Color.BLACK)
        self.root = self.NIL
        self.NIL.parent = self.NIL
        self.NIL.left = self.NIL
        self.NIL.right = self.NIL

    # *Rotations: Rotations are fundamental operations
    #           in maintaining the balanced structure of a Red-Black Tree (RBT). 
    #           They help to preserve the properties of the tree, ensuring that the longest path 
    #           from the root to any leaf is no more than twice the length of the shortest path. 
    #           Rotations come in two types: left rotations and right rotations.
    
    def left_rotation(self, node: Node):
        #  x                   y                           
        #   \                 / \                          
        #    y       ->      x   b                                            
        #  /  \               \                                      
        # a    b               a 
        right_child = node.right
        node.right = right_child.left

        if right_child.left != self.NIL:         
            right_child.left.parent = node
       
        right_child.parent = node.parent

        if node.parent == self.NIL:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        right_child.left = node
        node.parent = right_child

    def right_rotation(self, node: Node):
        #     x               y
        #    /               / \
        #   y       ->      a   x
        #  / \                 /
        # a   b               b
        left_child = node.left
        node.left = left_child.right

        if left_child.right != self.NIL:
            left_child.right.parent = node

        left_child.parent = node.parent

        if node.parent == self.NIL:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child

        left_child.right = node
        node.parent = left_child

    def fix_insert(self, new_node: Node):
        # While there are two continuos red nodes, we need to fix the tree
        while new_node.parent and new_node.parent.color == Color.RED:
            # If the parent of the left child of the grandparent of the new node is the parent of the new node
            if new_node.parent == new_node.grandparent().left:
                uncle = new_node.uncle()
                if uncle and uncle.color == Color.RED:
                    new_node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    new_node.grandparent().color = Color.RED
                    new_node = new_node.grandparent()
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.left_rotation(new_node)
                    new_node.parent.color = Color.BLACK
                    new_node.grandparent().color = Color.RED
                    self.right_rotation(new_node.grandparent())
            # If the parent of the right child of the grandparent of the new node is the parent of the new node
            else:
                uncle = new_node.uncle()
                if uncle and uncle.color == Color.RED:
                    new_node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    new_node.grandparent().color = Color.RED
                    new_node = new_node.grandparent()
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.right_rotation(new_node)
                    new_node.parent.color = Color.BLACK
                    new_node.grandparent().color = Color.RED
                    self.left_rotation(new_node.grandparent())
        self.root.color = Color.BLACK
    
    def fix_delete(self, node: Node):
        # While the node is not the root and the color of the node is black
        while node != self.root and node.color == Color.BLACK:
            # If the node is the left child of its parent
            if node == node.parent.left:
                sibling = node.sibling()
                if sibling.color == Color.RED:
                    sibling.color = Color.BLACK
                    node.parent.color = Color.RED
                    self.left_rotation(node.parent)
                    sibling = node.sibling()
                # If the color of the left child of the sibling of the node is black and the color of the right child of the sibling of the node is black
                if (sibling.left.color == Color.BLACK) and (sibling.right.color == Color.BLACK):
                    sibling.color = Color.RED
                    node = node.parent
                # If the color of the left child of the sibling of the node is black and the color of the right child of the sibling of the node is red
                else:
                    if sibling.right.color == Color.BLACK:
                        sibling.left.color = Color.BLACK
                        sibling.color = Color.RED
                        self.right_rotation(sibling)
                        sibling = node.sibling()

                    sibling.color = node.parent.color
                    node.parent.color = Color.BLACK
                    sibling.right.color = Color.BLACK
                    self.left_rotation(node.parent)
                    node = self.root
            else:
                # If the node is the right child of its parent
                sibling = node.sibling()
                # If the color of the sibling of the node is red
                if sibling.color == Color.RED:
                    sibling.color = Color.BLACK
                    node.parent.color = Color.RED
                    self.right_rotation(node.parent)
                    sibling = node.sibling()
                # If the color of the left child of the sibling of the node is black and the color of the right child of the sibling of the node is black
                if (sibling.left.color == Color.BLACK) and (sibling.right.color == Color.BLACK):
                    sibling.color = Color.RED
                    node = node.parent
                # If the color of the right child of the sibling of the node is black and the color of the left child of the sibling of the node is red
                else:
                    if sibling.left.color == Color.BLACK:
                        sibling.right.color = Color.BLACK
                        sibling.color = Color.RED
                        self.left_rotation(sibling)
                        sibling = node.sibling()

                    sibling.color = node.parent.color
                    node.parent.color = Color.BLACK
                    sibling.left.color = Color.BLACK
                    self.right_rotation(node.parent)
                    node = self.root
        # Set the color of the node to black
        node.color = Color.BLACK

    def replace_node(self, old_node, new_node):
        if old_node.parent == self.NIL:
            self.root = new_node
        elif old_node == old_node.parent.left:
            old_node.parent.left = new_node
        else:
            old_node.parent.right = new_node
        new_node.parent = old_node.parent

    #Q.1: Implement the insert, deleteVal and printInOrder methods for the Red-Black Tree
    def insert(self, key):
        """Inserts a new node with the specified key into the Red-Black Tree."""
        new_node = self.Node(key)
        new_node.parent = self.NIL
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent_node = self.NIL
        curr_node = self.root
        while curr_node != self.NIL:
            # While the current node is not NIL, we traverse the tree to find the correct position for the new node
            parent_node = curr_node
            if new_node.key < curr_node.key:
                # If the key of the new node is less than the key of the current node, we move to the left child
                curr_node = curr_node.left
            else:
                # If the key of the new node is greater than or equal to the key of the current node, we move to the right child
                curr_node = curr_node.right
        new_node.parent = parent_node
        if parent_node == self.NIL:
            # If the parent node is NIL, the new node is the root of the tree
            self.root = new_node
        elif new_node.key < parent_node.key:
            # If the key of the new node is less than the key of the parent node, the new node is the left child of the parent node
            parent_node.left = new_node
        else:
            # If the key of the new node is greater than or equal to the key of the parent node, the new node is the right child of the parent node
            parent_node.right = new_node
        self.fix_insert(new_node)
        
    def delete_val(self, key):
        """Removes the node with the specified key from the Red-Black Tree."""
        node_to_delete = self.find(key)
        if node_to_delete == self.NIL:
            return  # Node not found

        successor_node = node_to_delete
        original_color = successor_node.color
        # If the node to delete has only one child, we replace the node with its child
        if node_to_delete.left == self.NIL:
            child_node = node_to_delete.right
            self.replace_node(node_to_delete, node_to_delete.right)
        # If the node to delete has only one child, we replace the node with its child
        elif node_to_delete.right == self.NIL:
            child_node = node_to_delete.left
            self.replace_node(node_to_delete, node_to_delete.left)
        # If the node to delete has two children, we find the successor node and replace the node with the successor node
        else:
            successor_node = self.find_min(node_to_delete.right)
            original_color = successor_node.color
            child_node = successor_node.right
            if successor_node.parent == node_to_delete:
                child_node.parent = successor_node
            else:
                self.replace_node(successor_node, successor_node.right)
                successor_node.right = node_to_delete.right
                successor_node.right.parent = successor_node
            self.replace_node(node_to_delete, successor_node)
            successor_node.left = node_to_delete.left
            successor_node.left.parent = successor_node
            successor_node.color = node_to_delete.color

        if original_color == Color.BLACK:
            self.fix_delete(child_node)


    def print_in_order(self, node):
        if node != self.NIL:
            self.print_in_order(node.left)
            print(f"{node.key}({node.color.value})", end=" ")
            self.print_in_order(node.right)

    #Q.2: Implement find(find a specific key), find_min(find the lowest key) and find_max(find the greatest key) methods
    def find(self, key):
        curr_node = self.root
        while curr_node is not self.NIL:
            if key == curr_node.key:
                return curr_node
            elif key < curr_node.key:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return self.NIL
    
    def find_min(self, node):
        while node.left != self.NIL:
            node = node.left
        return node
    
    def find_max(self, node):    
        while node.right != self.NIL:
            node = node.right
        return node

if __name__ == "__main__":
    tree = RedBlackTree()
    #Q.6: Execute the operations and print the inorder of the Red-Black Tree after each operation
    # 1. Insert the keys [5, 16, 22, 45, 2, 10, 18, 30, 50, 12, 1] into the Red-Black Tree
    keys = [5, 16, 22, 45, 2, 10, 18, 30, 50, 12, 1]
    print("Inorder of the Red-Black Tree after inserting keys:")
    for key in keys:
        tree.insert(key)
    tree.print_in_order(tree.root)
    print("\n")
    # 2. Search for the keys 22 and 15 in the Red-Black Tree
    print("Searching for key 22:", tree.find(22))
    print("Searching for key 15:", tree.find(15))
    print("FindMin: ", tree.find_min(tree.root))
    print("FindMax: ", tree.find_max(tree.root))
    print("\n")
    # 3. Delete the keys 30, 10, and 22 from the Red-Black Tree. Insert the keys 25, 9, 33 and 50
    print("Inorder of the Red-Black Tree after deleting keys 30, 10, and 22:")
    tree.delete_val(30)
    tree.delete_val(10)
    tree.delete_val(22)
    tree.print_in_order(tree.root)
    print("\n")
    print("Inorder of the Red-Black Tree after inserting keys 25, 9, 33 and 50:")
    tree.insert(25)
    tree.insert(9)
    tree.insert(33)
    tree.insert(50)
    tree.print_in_order(tree.root)