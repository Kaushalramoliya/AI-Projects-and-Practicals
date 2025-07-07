'''  
@author: 22000409 Kaushal Ramoliya  
@description: 3. - Write a python program to create a binary tree, add elements, retrieve elements using pre
order, post-order and in-order traversal. 
'''  
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(self.root, value)

    def _add(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._add(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._add(current.right, value)

    def pre_order(self, node, result):
        if node:
            result.append(node.value)
            self.pre_order(node.left, result)
            self.pre_order(node.right, result)

    def in_order(self, node, result):
        if node:
            self.in_order(node.left, result)
            result.append(node.value)
            self.in_order(node.right, result)

    def post_order(self, node, result):
        if node:
            self.post_order(node.left, result)
            self.post_order(node.right, result)
            result.append(node.value)

if __name__ == "__main__":
    tree = BinaryTree()
    elements = [50, 30, 70, 20, 40, 60, 80] 

    for elem in elements:
        tree.add(elem)

    print("Binary Tree Traversals:")
    pre_order_result = []
    tree.pre_order(tree.root, pre_order_result)
    print("Pre-order Traversal:", pre_order_result)

    in_order_result = []
    tree.in_order(tree.root, in_order_result)
    print("In-order Traversal:", in_order_result)

    post_order_result = []
    tree.post_order(tree.root, post_order_result)
    print("Post-order Traversal:", post_order_result)