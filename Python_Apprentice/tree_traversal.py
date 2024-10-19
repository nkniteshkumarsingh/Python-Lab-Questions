class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value != value:
            if value < self.value:
                if self.left is None:
                    self.left = Tree(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Tree(value)
                else:
                    self.right.insert(value)

    def depth_traversal(self, node):
        items = []
        if node:
            items.append(node.value)
            items += self.depth_traversal(node.left)
            items += self.depth_traversal(node.right)
        return items

    def breadth_traversal(self, node):
        items = []
        if node:
            items += self.breadth_traversal(node.left)
            items.append(node.value)
            items += self.breadth_traversal(node.right)
        return items

    # def post_order_traversal(self, node):
    #     items = []
    #     if node:
    #         items += self.post_order_traversal(node.left)
    #         items += self.post_order_traversal(node.right)
    #         items.append(node.value)
    #     return items


if __name__ == "__main__":
    node = Tree(10)
    node.insert(5)
    node.insert(25)
    node.insert(12)
    node.insert(33)
    node.insert(18)

    print(f"Depth First Traversal: {node.depth_traversal(node)}")
    print(f"Breadth First Traversal: {node.breadth_traversal(node)}")
    # print(f"Post Order Traversal: {node.post_order_traversal(node)}")
