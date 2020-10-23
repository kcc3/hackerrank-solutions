"""Hackerrank Problem: https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem

A linked list is said to contain a cycle if any node is visited more than once while traversing the list. Given a
pointer to the head of a linked list, determine if it contains a cycle. If it does, return 1. Otherwise, return 0.
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


# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    """Function that detects if a linked list has a cycle in it

    Args:
        head (SinglyLinkedListNode): Head of the linked list to check for a cycle

    Returns:
        (int): 0 if there is not a cycle and 1 if there is
    """
    if head is None:
        return 0
    next_node = head
    double_node = head
    while double_node is not None and double_node.next is not None:
        next_node = next_node.next
        double_node = double_node.next.next
        if next_node == double_node:
            return 1
    return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        extra = SinglyLinkedListNode(-1);
        temp = llist.head;

        for i in range(llist_count):
            if i == index:
                extra = temp

            if i != llist_count - 1:
                temp = temp.next

        temp.next = extra

        result = has_cycle(llist.head)

        fptr.write(str(int(result)) + '\n')

    fptr.close()
