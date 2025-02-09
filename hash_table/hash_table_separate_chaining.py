# Q.1: Implement a hash table using separate chaining with colision treatment. The hash table should have the following methods: insert, remove, and find.
#      Insert the keys 5, 28, 19, 15, 20, 33, 12, 17, and 10 into the hash table. Take the size of the table as 9.

class HashTableSeparateChaining:
    class Node:
        def __init__(self, key):
            self.key = key
            self.next = None
    
    def __init__(self, size=9):
        self.size = size
        self.table = [None] * size
    
    def hash(self, key):
        """Hash function to calculate the index of the key."""
        return key % self.size
    
    def insert(self, key):
        """Insert a key into the hash table."""
        index = self.hash(key)
        if self.table[index] is None:
            self.table[index] = self.Node(key)
        else:
            curr_node = self.table[index]
            # Traverse the linked list to find the last node
            while curr_node.next is not None:
                # If the key is already present
                if curr_node.key == key:
                    return
                curr_node = curr_node.next
            if curr_node.key == key:
                return
            curr_node.next = self.Node(key)

    def remove(self, key):
        """Remove a key from the hash table."""
        index = self.hash(key)
        curr_node = self.table[index]
        prev_node = None
        # Traverse the linked list to find the key
        while curr_node is not None:
            # If the key is found
            if curr_node.key == key:
                # If the previous node is None, it means the key is the first node
                if prev_node is None:
                    self.table[index] = curr_node.next
                else:
                    prev_node.next = curr_node.next
                return
            # Move to the next node
            prev_node = curr_node
            curr_node = curr_node.next

    def print_table(self):
        """Print the hash table."""
        for i in range(self.size):
            print(f'{i}:', end=' ')
            curr_node = self.table[i]
            while curr_node is not None:
                print(curr_node.key, end=' -> ' if curr_node.next is not None else '')
                curr_node = curr_node.next
            print()
    
    def find(self, key):
        """Find a key in the hash table."""
        index = self.hash(key)
        curr_node = self.table[index]
        while curr_node is not None:
            if curr_node.key == key:
                return True
            curr_node = curr_node.next
        return False


if __name__ == '__main__':
    ht = HashTableSeparateChaining()
    keys = [5, 28, 19, 15, 20, 33, 12, 17, 10]
    for key in keys:
        ht.insert(key)
    print('Hash Table:\n')
    ht.print_table()
    print('\nFind 15:', ht.find(15))
    print('Find 25:', ht.find(25))
    ht.remove(33)
    print('\nHash Table after removing 15:\n')
    ht.print_table()
