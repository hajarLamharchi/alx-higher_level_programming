#!/usr/bin/python3
""" This class defines a node of a singly linked list """


class Node:
    """ This class defines a node of a singly linked list by
        Attributes:
        data (int): the data of the node
        next_node (Node): points to the next node
    """
    def __init__(self, data, next_node=None):
        """ Initializes a new instance of the Node class
            Parameters:
            data (int): the data of the node
            next_node (Node): points to the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Retrieves the value of data """
        return self.__data

    @data.setter
    def data(self, value):
        """ Sets the value of data """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Retrievs the value of next_node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Sets the value of next_node """
        if value != None and (not isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

""" This class defines a sigly linked list """
class SinglyLinkedList:
    """ This class defines a singly linked list by
        Attribute:
        head (Node): the head of the singly linked list
    """
    def __init__(self):
        """ Initializes a new instance of the SinglyLinkedList class """
        self.__head = None

    def sorted_insert(self, value):
        """ Inserts a new_node into the correct sorted position """
        nod = Node(value)
        if self.__head == None:
            self.__head = nod
        else:
            current = self.__head
            while current.next_node != None and current.data < value :
                current = current.next_node
            current










