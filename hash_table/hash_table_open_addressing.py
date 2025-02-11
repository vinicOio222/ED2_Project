# Q.2: Implement search, insertion, and deletion algorithms in a hash table 
# with collision handling using the open addressing method. 
# Consider inserting the keys (10, 22, 31, 4, 15, 28, 17, 88, 59) into a hash table of length m = 11 
# using open addressing with the auxiliary hash function h'(k) = k. Illustrate the result of inserting these keys using linear probing, using quadratic probing with
# c1 = 1 and c2 = 3, and using double hashing with h1(k) = k and h2(k) = 1 + (k mod (m - 1)).
#
# Repository Link - https://github.com/vinicOio222/ED2_Project/blob/main/hash_table/hash_table_open_addressing.py

class HashTable:
    def __init__(self, size):
        """ Initializes the hash table with a fixed size and fills it with None """
        self.size = size
        self.table = [None] * size
    
    def hash_default(self, k):
        """ 
        Primary hash function that determines the base position where the key should be inserted.
        Returns the calculated index as k % table size. 
        """
        return k % self.size
    
    def hash_alternative(self, k):
        """ 
        Secondary hash function used for double hashing. 
        Returns an offset based on 1 + (k % (m - 1)), ensuring a larger jump 
        and helping to better distribute the elements. 
        """
        return 1 + (k % (self.size - 1))
    
    def insert_linear(self, key):
        """ 
        Insertion using linear probing. 
        If a collision occurs, the next available position is searched sequentially (i + 1). 
        """
        index = self.hash_default(key)
        i = 0
        while self.table[(index + i) % self.size] is not None:
            i += 1  # Increments to check the next position
        self.table[(index + i) % self.size] = key
    
    def insert_quadratic(self, key, c1, c2):
        """ 
        Insertion using quadratic probing. 
        If a collision occurs, the offset grows quadratically (c1 * i + c2 * i²). 
        """
        index = self.hash_default(key)
        i = 0
        while self.table[(index + c1 * i + c2 * i**2) % self.size] is not None:
            i += 1  # Increments to try a new position
        self.table[(index + c1 * i + c2 * i**2) % self.size] = key
    
    def insert_double_hashing(self, key):
        """ 
        Insertion using double hashing. 
        If a collision occurs, a new offset is calculated using a second hash function. 
        """
        index = self.hash_default(key)
        step = self.hash_alternative(key)
        i = 0
        while self.table[(index + i * step) % self.size] is not None:
            i += 1  # Increments to test a new position
        self.table[(index + i * step) % self.size] = key
    
    def display(self):
        """ Displays the hash table showing the index and the stored value """
        for i, key in enumerate(self.table):
            print(f'Index {i}: {key}')


if __name__ == '__main__':
    # Definition of the table size and set of keys
    table_size = 11
    keys = [10, 22, 31, 4, 15, 28, 17, 88, 59]

    # Insertion using linear probing
    print("Linear Probing:")
    linear_table = HashTable(table_size)
    for key in keys:
        linear_table.insert_linear(key)
    linear_table.display()
    print("\n")

    # Insertion using quadratic probing
    print("Quadratic Probing:")
    quadratic_table = HashTable(table_size)
    for key in keys:
        quadratic_table.insert_quadratic(key, 1, 3)
    quadratic_table.display()
    print("\n")

    # Insertion using double hashing
    print("Double Hashing:")
    double_hash_table = HashTable(table_size)
    for key in keys:
        double_hash_table.insert_double_hashing(key)
    double_hash_table.display()
