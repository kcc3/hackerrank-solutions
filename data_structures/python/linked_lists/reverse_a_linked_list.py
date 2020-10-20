"""Hackerrank Problem: https://www.hackerrank.com/challenges/reverse-a-linked-list/problem

Given the pointer to the head node of a linked list, change the next pointers of the nodes so that their order is
reversed. The head pointer given may be null meaning that the initial list is empty.
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


# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse(head):
    """Function that reverses the order of a linked list

    Args:
        head (SinglyLinkedListNode): The head of the linked list to reverse

    Returns:
        (SinglyLinkedListNode): The head of the reversed linked list
    """
    current = head
    prev = None
    prev_two = None
    while current.next:
        prev_two = prev
        prev = current
        current = current.next
        # Set pointer
        prev.next = prev_two
    # Finally, set the last pointer for the new head of the reversed linked list
    current.next = prev
    return current


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_singly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
