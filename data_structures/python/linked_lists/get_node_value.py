"""Hackerrank Problem: https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem

Given a pointer to the head of a linked list and a specific position, determine the data value at that position. Count
backwards from the tail node. The tail is at postion 0, its parent is at 1 and so on.
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


# Complete the getNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def getNode(head, positionFromTail):
    """Function that gets the node information as specified from the position from the tail of the list

    Args:
        head (SinglyLinkedListNode): The head of a linked list to retrieve data from
        positionFromTail (int): The integer position from the tail of the list which we want to retrieve data from

    Returns:
        (int): The data for the specified node
    """
    counter = 0
    traverse = head
    while traverse.next is not None:
        counter += 1
        traverse = traverse.next
    pos = counter - positionFromTail
    for i in range(pos):
        head = head.next
    return head.data


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        position = int(input())

        result = getNode(llist.head, position)

        fptr.write(str(result) + '\n')

    fptr.close()
