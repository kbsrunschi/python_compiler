'''
Kathryn Smith 
Purpose: Create doubly linked list class object for python
for use in compiler
 
Source: https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python
Additional help from
http://stackoverflow.com/questions/15710895/doubly-linked-list-iterator-python
http://ls.pwd.io/2014/08/singly-and-doubly-linked-lists-in-python/
'''
 
class Node(object):
 
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node
        if self.prev_node is None:
            self.offSet = 0
        else:
            self.offSet = prev_node.offSet 
 
    def __str__(self):
        return "Node: %s" %self.data
 
    def get_data(self):
        return self.data
 
    def get_next(self):
        return self.next_node
 
    def set_next(self, next_node):
        self.next_node = next_node
 
    def get_prev(self):
        return self.prev_node
 
    def set_prev(self, prev_node):
        self.prev_node = prev_node
 
    def get_offset(self):
        return self.offSet
 
    def set_offset(self, offset):
        self.offSet = offset
 
class ListIterator(object):
    def __init__(self, node):
        self.current = node
  
    def __iter__(self):
        return self
  
    def next(self):
        if self.current is None:
            raise StopIteration()
        result = self.current.data
        self.current = self.current.prev_node
        return result
 
class LinkedList(object):
 
    def __init__(self, head=None, tail=None):
        global offset
        self.head = head
        self.tail = tail
        self.currentNode = None
 
    def __iter__(self):
        return ListIterator(self.tail)
 
    def insert(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev_node = self.tail
            new_node.next_node = None  #want to set as new tail
            self.tail.next_node = new_node
            self.tail = new_node  #key tail as a real value and not None
 
    def delete(self):
        #delete the tail node only
        #offset = offset - self.size(self.tail) #need to delete offset when fall out of scope
        currentNode = self.tail
        if currentNode is None:
            raise ValueError("Tail is empty")
        previous = currentNode.prev_node
        if previous is None:
            self.head = self.tail = None
            print "List is now empty"
        else:
            previous.set_next(None)
            self.tail = previous
 
    def clear_all(self):
        currentNode = self.tail
        previous = currentNode.prev_node
        if previous is None:
            self.head = self.tail = None
            print "List is now empty"
        else:
            while previous is not None:
                previous.set_next(None)
                currentNode = previous
                previous = currentNode.prev_node
            self.head = self.tail = None
            print "List is now empty"
 
    def findDefined(self, node):
        currentNode = self.head
        #determine if a node identifier is already in the stack
        while currentNode is not None:
            for key in currentNode.data:
                if key == node:
                    return currentNode
            currentNode = currentNode.next_node
    def isDefined(self, node):
        currentNode = self.head
        #determine if a node identifier is already in the stack
        isDefined = False
        while currentNode is not None:
            for key in currentNode.data:
                if key == node:
                    isDefined = True
            currentNode = currentNode.next_node
        return isDefined
 
    def printList(self):
        if self.head is not None:
            print "Here is your linked list: "
            currentNode = self.head
            while currentNode is not None:
                print currentNode
                currentNode = currentNode.next_node
        else:
            print "Your linked list is empty. \nI hope this is what you wanted!"
 
    def getType(self, node):
        currentNode = self.head
        while currentNode is not None:
            for key in currentNode.data:
                if key == node:
                   keyType = currentNode.data.get(key)
            currentNode = currentNode.next_node
        return keyType
 
 
    def getNode(self, node):
        currentNode = self.head
        while self.isDefined(node) is False:
            currentNode = currentNode.next_node
        return currentNode