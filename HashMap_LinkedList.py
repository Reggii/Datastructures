# !Python 3.10
# Rihhard Elm
# -------------
# This is an implementation of a hash map linked list in Python with the following functionality:
# - Insert
# - Find
# - Delete
# - Print
# ------------------------------- Hash map linked list implementation ------------------------------------ #
class Node:
    """
    We construct the Node class with a key-value pair as well as a next parameter.
    The next parameter is by default set to None, and we can in case of a collision configure as a pointer.
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return str((self.key, self.value))

class HashTable:
    """
    We construct our HashTable class with a predefined size and a list of buckets.
    The list of buckets is multiplied by the size which we will then use to store our values.
    """
    def __init__(self):
        self.size = 12
        self.buckets = [None] * self.size

    def _get_hash(self, key):
        """
        We pass our key as an argument to the _get_hash function which then iterates over each character in the key.
        Upon each iteration we add together the index, length of our key and then multiply their sum to the
        power of the unicode key to our current character, giving us a unique number for each character.

        We sum each unique number into the key_hash variable which we then modulate by our previously defined -
        list size, so we can use that for accessing our key-value pair in the list.
        """
        key_hash = 0

        for i, v in enumerate(key):
            key_hash += (i + len(key)) ** ord(v)
        key_hash = key_hash % self.size

        return key_hash

    def insert(self, key, value):
        """
        The insert function will first generate the hash for our key and store it as position since it's a valid index.
        We store our node as the location for where we can store our key-value pair.

        If our node location points to None, we replace it with a Node object constructed with our key-value pair.

        If the node location points to a value, we are dealing with a collision and can make use of our linked list.
        The prev is set to node, so we can save our starting position and keep track of the current position.
        We then loop through the linked list (or more specifically our next pointers) until either:
        A) Our next pointer points to None, in which case we set our next pointer to a Node object containing our key-value pair
        B) Our current nodes key matches the key we wish to insert, in which case we update the value of the key and return
        """
        position = self._get_hash(key)
        node = self.buckets[position]

        if node is None:
            self.buckets[position] = Node(key, value)
            return

        prev = node
        while node is not None:
            if node.key == key:
                node.value = value
                print(f'Key: {key} value updated to {value}')
                return
            prev = node
            node = node.next
        prev.next = Node(key, value)

    def find(self, key):
        """
        See the insert function for an elaboration on position and node

        We go to our hashed position in the constructed list and attempt a while loop which reveals to us
        whether the positioned node or any of its next pointers contain our key

        If the next pointer points to None and the hashed position did not contain our key, we print 'not in list'.
        Otherwise, we print that the key was located together with its value.
        """
        position = self._get_hash(key)
        node = self.buckets[position]

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            print(f'Key: {key} not in list')
            return
        else:
            print(f'Key: {key} in list with value {node.value}')
            return

    def delete(self, key):
        """
        See the insert function for an elaboration on position and node

        We track our previous and current position with the variable prev, which starts as None.
        We attempt a while loop similarly to the find function to determine whether our current node contains our key
        or if not, whether its next pointer contains any key-value pairs we can check.

        If we exit the loop and our node is none, we did not find our key and print the statement accordingly.

        If our node key is a match, we check first if we went through a linked list loop by confirming whether prev is None.
        If prev is none we simply set the position of our key-value pair to None.
        Otherwise, we set the next pointer of prev to None.
        """
        position = self._get_hash(key)
        node = self.buckets[position]
        prev = None

        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            print(f'Key {key} not in list')
            return
        else:
            if prev is None:
                self.buckets[position] = None
            else:
                prev.next = None
            return

    def print(self):
        """
        The print statement stores our position in the iteration through the length of the list starting from 0.
        
        At each iteration we set our node value to the position, check if node is not None, we print the value,
        then check if the node points to another node, in which case we print the next nodes value and set it as our current node
        to check for any further links.
        
        After each iteration we increment the position by 1, effectively going through the whole list.
        """
        position = 0
        for i in range(0, len(self.buckets)):
            node = self.buckets[position]
            if node:
                print(node, end='\n')
                while node.next:
                    print(node.next, end='\n')
                    node = node.next
            position += 1
        print('# ----------- #')

if __name__ == '__main__':
    # Instantiate the class    
    h = HashTable()
    # Test the insert, find and print functionality
    h.insert('Bob', '550-889')
    h.insert('John', '510-819')
    h.insert('Jill', '110-119')
    h.insert('Damian', '919-127')
    h.find('John')
    h.find('Jill')
    h.print()
    # Test the insert/update functionality
    h.insert('Jill', '121-119')
    h.print()
    # Test the find and delete functionality
    h.find('Albert')
    h.delete('Jill')
    h.find('Jill')
    h.print()
