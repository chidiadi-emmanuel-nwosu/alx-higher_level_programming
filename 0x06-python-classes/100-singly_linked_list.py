#!/usr/bin/python3
# File: 100-singly_linked_list.py
# Author: Chidiadi E. Nwosu

"""Defines a node in a singly linked list"""


class Node:
    """A node class"""

    def __init__(self, data, next_node=None):
        """initializes a new node

        Args:
            dat (int): element in the node
            next_node (node): pointer to the next element
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """returns the element of the node"""

        return self.__data

    @data.setter
    def data(self, value):
        """sets the element of the newly created node

        Args:
            value: input parameter for the element
        """

        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """returns the next_node of the linkedlist"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the position of the newly created square

        Args:
            value: input parameter for position
        """

        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


"""Defines the linkedlist"""


class SinglyLinkedList:
    """A node head"""

    def __init__(self):
        """the head of the linkedlist"""

        self.__head = None

    def sorted_insert(self, value):
        """inserts a new node into the correct sorted position in the list

        Args:
            value: value to insert into the list
        """

        new = Node(value)

        if self.__head is None or self.__head.data >= value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head

            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """returns the string representation of the linked list"""

        linked_list = []
        tmp = self.__head

        while tmp is not None:
            linked_list.append(str(tmp.data))
            tmp = tmp.next_node

        return "\n".join(linked_list)
