"""Hackerrank Problem: Hackerrank Problem: https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem

Given a reference to the head of a doubly-linked list and an integer, data, create a new DoublyLinkedListNode object
having data value data and insert it at the proper location to maintain the sort.
"""

import math
import os
import random
import re
import sys


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    """Insert the data into the sorted doubly linked list at the correct sorted location

    Args:
        head (DoublyLinkedListNode): Head of the doubly linked list to insert into
        data (int): integer data to store

    Returns:
        (DoublyLinkedListNode): The head of the doubly linked list with newly inserted node
    """
    # If head is empty, or we need to create a new node that's the head of the list
    node = DoublyLinkedListNode(data)
    if head is None or head.data > data:
        head.prev = node
        node.next = head
        return node
    # Else, traverse to find the location we need to insert new node
    cur = head
    prev = None
    while cur is not None and cur.data < data:
        prev = cur
        cur = cur.next

    # Adjust pointers to insert the new node
    node.prev = prev
    node.next = prev.next
    prev.next = node

    return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
