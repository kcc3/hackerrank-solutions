"""Hackerrak Problem: https://www.hackerrank.com/challenges/tree-preorder-traversal/problem

Complete the preOrder function in your editor below, which has 1 parameter: a pointer to the root of a binary tree. It
must print the values in the tree's preorder traversal as a single line of space-separated values.
"""


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def preOrder(root):
    """Hackerrank Problem: https://www.hackerrank.com/challenges/tree-preorder-traversal/problem

    Function to print out the values of the tree in preorder, so traversing the tree starting from the root and
    recursively traversing the left subtree and then right subtree

    Args:
        root (Node): Root of the tree

    Returns:
        None
    """
    if root:
        print(root.info, end=" ")
    if root.left:
        preOrder(root.left)
    if root.right:
        preOrder(root.right)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

preOrder(tree.root)