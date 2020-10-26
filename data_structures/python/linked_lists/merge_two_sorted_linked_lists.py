"""Hackerrank Problem: https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem

Given pointers to the heads of two sorted linked lists, merge them into a single, sorted linked list. Either head
pointer may be null meaning that the corresponding list is empty.
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


# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    """Marge two sorted linked lists into one

    Args:
        head1 (SinglyLinkedListNode): The head of the first linked list
        head2 (SinglyLinkedListNode): The head of the second linked list

    Returns:
        (SinglyLinkedListNode): The head of the merged linked list
    """
    # Check for empty lists first, return None if both lists are empty
    if head1 is None and head2 is None:
        return None
    # If head1 is empty and head2 is a list, return the second list
    if head1 is None:
        return head2
    # If head1 is a list and head2 is empty, return the first list
    if head2 is None:
        return head1
    # Else, merge the lists together
    travel = None
    merge = None
    head = None
    # We use the list with the smaller first value as our stationary list, and travel through the other
    if head1.data < head2.data:
        travel = head2
        merge = head1
        head = head1
    else:
        travel = head1
        merge = head2
        head = head2
    # Go through the travel list and marge it into the stationary list
    while travel:
        if merge.data <= travel.data:
            if merge.next is None:
                merge.next = travel
                break
            elif merge.next.data >= travel.data:
                node = SinglyLinkedListNode(travel.data)
                node.next = merge.next
                merge.next = node
                travel = travel.next
            else:
                merge = merge.next
    return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()
