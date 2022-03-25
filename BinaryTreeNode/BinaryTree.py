class BinaryTree:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

    def add_child(self, data):
        if self.data == data:
            return
        
        if self.data < data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTree(data)
        else:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTree(data)

    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)
        
        return self

    # left tree --> root node --> right tree
    def in_order_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.in_order_traversal()
        
        elements.append(self.data)
        
        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements

    # root node --> left tree --> right tree
    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()
        
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    # left tree --> right tree --> root node
    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def search(self, data):
        if self.data == data:
            return True

        if self.data < data:
            if self.right:
                return self.right.search(data)
            else:
                return False

        if self.data > data:
            if self.left:
                return self.left.search(data)
            else:
                return False

    def __contains__(self, data):
        return self.search(data)

    def calculate_sum(self):
        return sum(self.in_order_traversal())

    def find_min(self):
        if self.left.left == None:
            return self.left.data

        if self.left:
            return self.left.find_min()

    def find_max(self):
        if self.right.right == None:
            return self.right.data

        if self.right:
            return self.right.find_max()

if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers = [15, 12, 7, 14, 27, 20, 23, 88]

    numbers_tree = BinaryTree(numbers[0])

    for i in numbers[1:]:
        numbers_tree.add_child(i)

    print("Input numbers:",numbers)
    print("Min:",numbers_tree.find_min())
    print("Max:",numbers_tree.find_max())
    print("Sum:", numbers_tree.calculate_sum())
    print("In order traversal:", numbers_tree.in_order_traversal())
    print("Pre order traversal:", numbers_tree.pre_order_traversal())
    print("Post order traversal:", numbers_tree.post_order_traversal())  
    numbers_tree.delete(27)
    print("Delete 23 from the tree:", numbers_tree.in_order_traversal())