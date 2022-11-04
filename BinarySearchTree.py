
# !Python 3.10
#  Rihhard Elm
# ------------- 
# This is an implementation of a binary search tree in Python with the following functionality:
# - Insert
# - Find
# - Delete
# - Traverse (In/Pre/Postorder)
# ------------------------------- Binary search tree implementation ------------------------------------ #

class BinaryNode:
    # The node class is initiated with a value and two pointers, left and right
    def __init__(self, value):
        self.value = value
        self.left = None # Left will point to the smaller node
        self.right = None # Right will point to the larger node

class BinarySearchTree:
    # The tree is always initiated with the root being None
    def __init__(self):
        self.root = None

    @staticmethod # Find a successor for our node deletion
    def find_successor(root):
        # If our root.right is None - we traverse the left subtrees full height for the successor
        if root.right is None:
            pointer = root.left
        # If our root.left is None - we start our traversal from the right node and then
        # we traverse the left subtrees full height
        else:
            pointer = root.right
        # The while loop is where we do the traversal
        while pointer.left is not None:
            pointer = root.left
        return pointer

# ------------------- Insert ------------------- #
    # We start our tree by inserting our values using the insert function
    def insert(self, value):
        # If the root for the class is None, our current value will be set as the root
        if self.root is None:
            self.root = BinaryNode(value)
            return self.root
        # If the root is not None, we call the inner _insert function with our root and value
        else:
            self._insert(self.root, value)

    def _insert(self, root, value):
        # We compare the root with the value we wish to insert
        if value < root.value:
            # If our value is smaller than the root and root.left/right already points to None
            # we simply set our value to the pointer as a Node object
            if root.left is None:
                root.left = BinaryNode(value)
            # Otherwise, we recursively call upon the left node until we find None
            else:
                root.left = self._insert(root.left, value)
        # Vice versa as above for the right pointer if the value is bigger
        if value > root.value:
            if root.right is None:
                root.right = BinaryNode(value)
            else:
                root.right = self._insert(root.right, value)
        return root

# ------------------- Find ------------------- #
    # Our find function takes our value as the parameter
    def find(self, value):
        # If self.root is None, our tree is empty
        if self.root is None:
            return 'This tree is empty'
        else:
        # Else we pass our root and value as arguments to the inner _find function
            self._find(self.root, value)

    def _find(self, root, value):
        # If our root returns None
        # this means that we have traversed the height of the tree
        # without finding our value
        if root is None:
            print('\n')
            print('Value not in tree')
            return
        # If value is smaller than root, we recursively call upon the left pointer
        if value < root.value:
            self._find(root.left, value)
        # If value is bigger than root, we recursively call upon the left pointer
        elif value > root.value:
            self._find(root.right, value)
        # If value matches the root, we return a confirmation
        elif value == root.value:
            print('Value in tree')
            return

# ------------------- Delete ------------------- #
    # Delete a node in the tree
    def delete(self, value):
        # If our root is None, the tree is empty with nothing to delete
        if self.root is None:
            return 'Tree is empty'
        else:
        # Otherwise we call our inner _delete function passing in our root and value as parameters
            self._delete(self.root, value)

    def _delete(self, root, value):
        # If root is None, we will return None, effectively changing the Node value to none (deleting it)
        if not root:
            return None
        # First we compare if our value is smaller or bigger than the root
        # and recursively traverse the tree accordingly until we get a match or our root returns None
        if value < root.value:
            root.left = self._delete(root.left, value)
        elif value > root.value:
            root.right = self._delete(root.right, value)
        # Once our value is found we have 4 different cases that we can encounter
        elif value == root.value:
            # If the node has neither a left nor right child, we set it to None
            if not root.left and not root.right:
                return None
            # If it has a right child, but not a left child, we set its value to the right child
            elif not root.left and root.right:
                return root.right
            # If it has a left child, but not a right child, we set its value to the left child
            elif not root.left and root.right:
                return root.left
            # If however, it has both a left and a right child, we want to swap it with the
            # successor - the logic for finding the successor is defined in the find_successor function
            elif root.left and root.right:
                get_successor = self.find_successor(root)
                # Once we have our successor node, we set it as our root
                root.value = get_successor.value
                # Then we make sure to traverse both subtrees and remove our successor's duplicate
                # We traverse both since our successor might have been from either of the subtrees
                root.left = self._delete(root.left, get_successor.value)
                root.right = self._delete(root.right, get_successor.value)
        return root

# ------------------- Traverse ------------------- #
    # We start our inorder traversal
    def inorder(self):
        # If root is None we return that the tree is empty
        if self.root is None:
            return 'Tree is empty!'
        else:
            print('\n')
        # We call the inner function with our root as the argument to complete traversal
            self._inorder(self.root)

    def _inorder(self, root):
        # This is our recursive base case, if we reach it we return the calls we have made
        if root is None:
            return
        # We first traverse the height of all the left nodes recursively
        self._inorder(root.left)
        # Then their values are printed based on the recursive stack principle(!)
        # Last in - first out
        print(f'{root.value}', end=' ')
        # Same for the right subtree
        self._inorder(root.right)

    # Preorder follows the same logic as inorder, however we print the value before the recursive call
    def preorder(self):
        if self.root is None:
            return 'Tree is empty!'
        else:
            print('\n')
            self._preorder(self.root)

    def _preorder(self, root):
        if root is None:
            return
        print(f'{root.value}', end=' ')
        self._preorder(root.left)
        self._preorder(root.right)

    # With postorder we print the value after both recursive calls
    def postorder(self):
        if self.root is None:
            return 'Tree is empty!'
        else:
            print('\n')
            self._postorder(self.root)

    def _postorder(self, root):
        if root is None:
            return
        self._postorder(root.left)
        self._postorder(root.right)
        print(f'{root.value}', end=' ')


if __name__ == '__main__':
    # We take a random list of integers
    keys = [20, 10, 30, 15, 35, 25, 9, 32, 7]
    # We initialize our Binary Search Tree class
    bst = BinarySearchTree()
    # We loop over our list and insert the items, creating nodes
    for key in keys:
        bst.insert(key)
    # We test that our values are inserted and inorder prints correctly
    bst.inorder()
    # We test our delete function
    bst.delete(30)
    bst.inorder()
    # We test our find function
    bst.find(33)
    bst.find(9)
    # We test our traversals
    bst.preorder()
    bst.postorder()
