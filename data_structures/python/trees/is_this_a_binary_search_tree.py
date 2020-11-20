"""Hackerrank Problem: https://www.hackerrank.com/challenges/is-binary-search-tree/problem

For the purposes of this challenge, we define a binary tree to be a binary search tree with the following ordering
requirements:

* The data value of every node in a node's left subtree is less than the data value of that node.
* The data value of every node in a node's right subtree is greater than the data value of that node.

Given the root node of a binary tree, can you determine if it's also a binary search tree?

Complete the function in your editor below, which has 1 parameter: a pointer to the root of a binary tree. It must
return a boolean denoting whether or not the binary tree is a binary search tree. You may have to write one or more
helper functions to complete this challenge.
"""

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""


def inorder_traversal(root):
    """Function to traverse a binary tree inorder

    Args:
        root (Node): The root of a binary tree

    Returns:
        (list): List containing all the values of the tree from an inorder search
    """
    res = []
    if root:
        res = inorder_traversal(root.left)
        res.append(root.data)
        res = res + inorder_traversal(root.right)
    return res


def check_binary_search_tree_(root):
    """Function to determine if the tree satisfies the condition to be a binary search tree

    Args:
        root (Node): The root of the binary tree to check

    Returns:
        (bool): Whether the tree is a binary search tree or not
    """
    res = inorder_traversal(root)
    return res == sorted(res) and len(res) == len(set(res))
