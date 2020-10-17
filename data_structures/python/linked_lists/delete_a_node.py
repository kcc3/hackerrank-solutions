"""Hackerrank Problem: https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem

Delete the node at a given position in a linked list and return a reference to the head node. The head is at position 0.
The list may be empty after you delete the node. In that case, return a null value.
"""

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    """Function to remove a node from the linked list at the specified position

    Args:
        head (SinglyLinkedListNode): The head of the linked list
        position (int): The position of the node to delete

    Returns:
        (SinglyLinkedListNode): The head of the new linked list after removing the specified node
    """
    if position == 0:
        return head.next
    cur_node = head
    prev_node = None
    for i in range(position):
        prev_node = cur_node
        cur_node = cur_node.next
    prev_node.next = cur_node.next
    return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    position = int(input())

    llist1 = deleteNode(llist.head, position)

    print_singly_linked_list(llist1, ' ', fptr)
    fptr.write('\n')

    fptr.close()
