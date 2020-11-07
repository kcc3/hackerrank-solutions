"""Hackerrank Problem: https://www.hackerrank.com/challenges/queue-using-two-stacks/problem

A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest
elements to be removed from the front and new elements to be added to the rear. This is called a First-In-First-Out
(FIFO) data structure because the first element added to the queue (i.e., the one that has been waiting the longest) is
always the first one to be removed.

A basic queue has the following operations:

Enqueue: add a new element to the end of the queue.
Dequeue: remove the element from the front of the queue and return it.

In this challenge, you must first implement a queue using two stacks. Then process q queries, where each query is one
of the following 3 types:

1 x: Enqueue element x into the end of the queue.
2: Dequeue the element at the front of the queue.
3: Print the element at the front of the queue.
"""


class HackerrankQueue(object):
    """Hackerrank Queue class

    Attributes:
        s1: First stack used to manage queue
        s2: Second stack used to manage queue
    """

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, value):
        """Add a value to the back of the queue

        Args:
            value: The data to add to the back of the queue

        Returns:
            None
        """
        self.s1.append(value)

    def dequeue(self):
        """Remove and return the value at the front of the queue

        Args:
            None

        Returns:
            (int): The value at the front of the queue
        """
        if not self.s2:
            for _ in range(len(self.s1)):
                self.s2.append(self.s1.pop())
        if self.s2:
            return self.s2.pop()
        else:
            return None

    def front(self):
        """Return the value at the front of the queue

        Args:
            None

        Returns:
            (int): Value at the front of the queue
        """
        if not self.s2:
            for _ in range(len(self.s1)):
                self.s2.append(self.s1.pop())
            return self.s2[-1]
        else:
            return self.s2[-1]


if __name__ == "__main__":
    h = HackerrankQueue()
    h.enqueue(42)
    h.dequeue()
    h.enqueue(14)
    print(h.front())
    h.enqueue(28)
    print(h.front())
    h.enqueue(60)
    h.enqueue(78)
    h.dequeue()
    h.dequeue()
