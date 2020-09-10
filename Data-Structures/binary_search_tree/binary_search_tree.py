"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from doubly_linked_list import DoublyLinkedList
from queue import Queue
from stack import Stack


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    #add left add right?

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)
            # elif self.value < value:
            #     self.left.insert(value)

        else:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value is target:
            return True
        
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        # if self.right:
        #     return self.right.get_max()
        # else:
        #     return self.value

        if not self:
            return None
        while self.right:
            self = self.right
        return self.value

    def get_min(self):
        if not self:
            return None
        while self.left:
            self = self.left
        return self.value
            

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):  #shouldn't take another parameter
        # queue = Queue()
        # queue.enqueue(node)    #self.left, self.right
         
        if self.left is not None:
            self.left.in_order_print()
        print(self.value)
        if self.right is not None:
            self.right.in_order_print()



    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        """instantiate a queue"""
        queue = Queue()
        """enqueue starting node (self)"""
        queue.enqueue(self)

        """while the queue is not empty dequeue the sarting node"""
        while len(queue) > 0:
            self = queue.dequeue()  
            print(self.value)
            if self.left:
                queue.enqueue(self.left)  #enqueue left child
            if self.right:
                queue.enqueue(self.right)
    

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        """instantiate a stack"""
        stack = Stack()
        """push starting node (self)"""
        stack.push(self)
        """while the stack is not empty pop the sarting node"""
        while len(stack) > 0:
            self = stack.pop()
            print(self.value)
            if self.left:
                stack.push(self.left)
            if self.right:
                stack.push(self.right)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    # def pre_order_dft(self):
    #     pass

    # Print Post-order recursive DFT
    # def post_order_dft(self):
    #     pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

#bst.in_order_print
#bst.bft_print()
bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
