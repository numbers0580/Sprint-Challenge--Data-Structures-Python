class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            # LEFT
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            # RIGHT
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        if target < self.value:
            # LEFT
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else: 
            # RIGHT
            if not self.right:
                return False
            else:
                return self.right.contains(target)

                

    # Return the maximum value found in the tree
    #used recursion - function that calls itself
    #run time O (log n)
    def get_max(self):
        #check to the right side of the tree
        #since left (self.left.value) side of the tree will always be smaller than the root

        #if the right side of the tree is empty that just return the tree
        if not self.right:
            return self.value
        #if right side of the tree is not empty. Then get the right child node with the max value
        else:
            return self.right.get_max()


    # Call the function `fn` on the value of each node

    #example of a tree traversal. Want to traverse through every tree node
    #recursion
    #doesn't actually return anything 
    def for_each(self, fn):
       #call the function `fn` on self.value
       fn(self.value)
        #go to right child nodes if any exists
       if self.right:
           self.right.for_each(fn)
       #go to the left child nodes if any exists
       if self.left:
           self.left.for_each(fn)