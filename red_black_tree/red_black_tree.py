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
            return f"{self.key} ({self.color})"
        
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

        if left_child.left != self.NIL:
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
    
    def find_min(self, node: Node):
        pass

    def fix_delete(self, node: Node):
        pass

    #Q.1: Implement the insert, deleteVal and printInOrder methods for the Red-Black Tree
    def insert(self, key):
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
        

    def deleteVal(self, key):
        pass

    def printInOrder(self, node):
        if node != self.NIL:
            self.printInOrder(node.left)
            print(f"{node.key}({node.color.value})", end=" ")
            self.printInOrder(node.right)


if __name__ == "__main__":
    tree = RedBlackTree()
    #Q.6: Execute the operations and print the inorder of the Red-Black Tree after each operation
    # 1. Insert the keys [5, 16, 22, 45, 2, 10, 18, 30, 50, 12, 1] into the Red-Black Tree
    keys = [5, 16, 22, 45, 2, 10, 18, 30, 50, 12, 1]
    print("Inorder of the Red-Black Tree:\n")
    for key in keys:
        tree.insert(key)
    tree.printInOrder(tree.root)
    print("\n")    



                