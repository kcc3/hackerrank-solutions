"""Hackerrank Problem: https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem

Given a pointer to the head of a linked list, insert a new node before the head. The next value in the new node should
point to head and the data value should be replaced with a given value. Return a reference to the new head of the list.
The head pointer given may be null meaning that the initial list is empty.
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


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(llist, data):
    """Function to insert a node at the head of a linked list

    Args:
        llist (SinglyLinkedListNode): The head of the current linkedlist
        data: The data to store in the list node

    Returns:
        head (SinglyLinkedListNode): The new head of the linkedlist
    """
    new_head = SinglyLinkedListNode(data)
    new_head.next = llist
    return new_head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()
