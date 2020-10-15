"""Hackerrank Problem: https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem

The height of a binary tree is the number of edges between the tree's root and its furthest leaf.

Complete the getHeight or height function in the editor. It must return the height of a binary tree as an integer.

getHeight or height has the following parameter(s):

root: a reference to the root of a binary tree.

Note -The Height of binary tree with single node is taken as zero.
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


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''


def height(root):
    """Function to return the height of a binary tree

    Args:
        root (Node): The root node of the binary tree

    Returns:
        (int): The height of the binary tree
    """
    left = 0
    right = 0
    if root.left:
        left = 1 + height(root.left)
    if root.right:
        right = 1 + height(root.right)
    return max(left, right)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))
