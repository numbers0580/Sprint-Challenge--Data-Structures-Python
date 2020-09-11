class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # Recursion visualization
        # assume a list of 3, 2, 1. We're sent 3, None
        # reverse_list(3, None)
        #     if node: # 3
        #         if node.get_next() == None: # false
        #             # skipping the code that would be here, obviously
        #         self.reverse_list(node.get_next(), node) -->
        #         RC(2, 3) <-- My short-hand for the above line
        #         if node: # 2
        #             if node.get_next() == None: # false
        #                 # skipping the code that would be here, obviously
        #             RC(1, 2)
        #             if node: # 1
        #                 if node.get_next() == None: # true
        #                     self.head = node # 1
        #                     self.head.next_node = prev # 1.next_node = 2
        #                     return <-- kick out so another RC(None, 1) is called, which would only return None
        #                 self.reverse_list(node.get_next(), node) # doesn't get called
        #                 node.next_node = prev # doesn't get called
        #             node.next_node = prev # node.next changes from 1 to 3
        #         node.next_node = prev # node.next changes from 2 to None

        if node:
            if node.get_next() == None:
                self.head = node
                self.head.next_node = prev
                return # <-- force an exit of this nested if node statement to prevent self.reverse_list(None, 1) from being called on next line, which would've caused an error
            self.reverse_list(node.get_next(), node)
            node.next_node = prev
