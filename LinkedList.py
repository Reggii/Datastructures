# !Python 3.10
#  Rihhard Elm
# -------------
# This is an implementation of a doubly linked list in Python with the following functionality:
# - Append
# - Prepend
# - Find
# - Delete
# - Print
#------------------------------- Linked List implementation in Python ------------------------------------

class ListNode:
    # We construct the node class, by default our next and prev pointers
    # are set to None
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    # We can use the __str__ method to return the string value of the node
    # which is useful for when we call a print function on the value
    def __str__(self):
        return str(self.value)

class LinkedList:
    # We construct the linked list class which takes no parameters
    # and by default has a head and tail parameters set to None
    def __init__(self):
        self.head = None
        self.tail = None

    # See ListNode __str__
    def __str__(self):
        return str(self)

    # The append function is where we start out our linked list construction
    def append(self, value):
        # We bind the passed value argument as a node object to a new variable called item
        item = ListNode(value)
        # If our head is None, this means our list is empty
        # in this case we set the value we passed as the head
        if self.head is None:
            self.head = item
            self.tail = item
            return item
        # Otherwise we call an inner append function with our item as the argument
        else:
            self._append(item)

    # The inner append function takes the value we wish to insert as an argument
    def _append(self, value):
        # Since we will start our iteration through the list from our tail node
        # we bind it to the variable current
        current = self.tail
        # We know that our tail nodes next pointer will always point to none
        # So we set the next pointer to value and we set our value previous pointer to current
        current.next = value
        value.prev = current
        # Since value is now our last node, we set our tail to value
        self.tail = value
        return value

    # The prepend function allows us to insert items at the front of the list
    def prepend(self, value):
        # We begin with creating a ListNode object with our value
        item = ListNode(value)
        # We check to see if our head is None, in which case we know the list is empty
        # So we set head and tail to the same value
        if self.head is None:
            self.head = item
            self.tail = item
            return item
        # If we have our head node set, we call the inner prepend function
        else:
            self._prepend(item)

    def _prepend(self, value):
        # We will position ourselves at the head node
        current = self.head
        # We know that our head nodes prev pointer will always point to none
        # So we set the prev pointer to value and we set our values next pointer to current
        current.prev = value
        value.next = current
        # Since value is now our head node, we set it accordingly
        self.head = value
        return value

    # The find function will loop over the list until we either find the value
    # that we pass as an argument or the next pointer is pointing to none
    def find(self, value):
        if self.head is None:
            return 'This list is empty'
        else:
            # Iteration starts from the head node
            current = self.head
            # Iteration runs until we find the value or next pointer points to None
            while current.value != value:
                if current.next is None:
                    print(f'Item {value} is not in the list')
                    return # Once the iteration ends we return
                current = current.next # In order to continue iterating we set the variable current to the next node
            print(f'Item {value} is in the list')

    # The delete_node function will look for the requested value in the linked list
    # and delete it if it is found, otherwise it will tell us that the item is not in the list
    def delete_node(self, value):
        # Iteration starts from the head node
        current = self.head
        # Iteration runs until we find the value or next pointer points to None
        while current.value != value:
            if current.next is None:
                print(f'Item {value} is not in the list')
                return
            current = current.next
        # We know we have found our value if we break out of the while loop
        # We then set the next value of the previous node to the next of the current node
        # and vice versa, thus deleting or "unlinking" our value
        current.prev.next = current.next
        current.next.prev = current.prev

    # This function prints a neat looking list with pointers showing
    # which value points to which
    def print_list(self):
        if self.head is None:
            return 'This is an empty list'
        else:
            current = self.head
            print('None ->', end=' ')
            while current.next is not None:
                print(f'{current.value}', end=' -> ')
                current = current.next
            print(f'{current.value} ->', end=' ')
            print('None')

    # This function is a more detailed view that prints all the pointer values
    # of every single node which can be useful to make sure that our pointers are set correctly
    def print_detail(self):
        if self.head is None:
            return 'This is an empty list'
        else:
            current = self.head
            while current.next is not None:
                print(f'Current node is {current.value}', end=' ')
                print(f'The previous node is {current.prev}', end=' ')
                print(f'The next node is {current.next}', end='\n')
                current = current.next
            print(f'Current node is {current.value}', end=' ')
            print(f'The previous node is {current.prev}', end=' ')
            print(f'The next node is None')


if __name__ == '__main__':
    # We construct our Linked List class under the linkedl variable
    linkedl = LinkedList()
    # We set-up an array with random integers
    keys = [20, 10, 12, 13, 14, 30, 22, 21, 32, 33, 35]
    # We loop over the integers and append them to our Linked List class
    for key in keys:
        linkedl.append(key)
    # We test the prepend functionality
    linkedl.prepend(5)
    # We test the print list functionality
    linkedl.print_list()
    # We test the find functionality
    linkedl.find(60)
    linkedl.find(22)
    # We test the delete functionality
    linkedl.delete_node(14)
    linkedl.print_list()
