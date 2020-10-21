"""Hackerrank Problem: https://www.hackerrank.com/challenges/compare-two-linked-lists/problem

You’re given the pointer to the head nodes of two linked lists. Compare the data in the nodes of the linked lists to
check if they are equal. If all data attributes are equal and the lists are the same length, return 1. Otherwise,
return 0.
"""
import os
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


# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):
    """Function that compares whether each node in two linked lists contain equivalent data

    Args:
        llist1 (SinglyLinkedListNode): The head for the first linked list
        llist2 (SinglyLinkedListNode): The head for the second linked list

    Returns:
        (int): 0 if the lists are not equal or 1 if they do contain equal data in each node
    """
    while True:
        if llist1.next is None and llist2.next is None:
            return 1
        elif llist1.next is None or llist2.next is None:
            return 0
        elif llist1.data != llist2.data:
            return 0
        llist1 = llist1.next
        llist2 = llist2.next


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

        result = compare_lists(llist1.head, llist2.head)

        fptr.write(str(int(result)) + '\n')

    fptr.close()
