# A Priority Queue is a Queue(anyList, compareTo)
# where Anylist is one of:
# None, or
# Pair(value, anyList)
class PriorityQueue:
    def __init__(self, list, comes_before):
        self.list = list
        self.comes_before = comes_before

    def __eq__(self, other):
        return (type(other) == PriorityQueue
                and self.list == other.list
                and self.comes_before == other.comes_before
                )

    def __repr__(self):
        return ("PriorityQueue({!r}, {!r})".format(self.list, self.comes_before))

# function -> PriorityQueue
# takes in an ordering function and returns an empty priority queue
def empty_pqueue(comes_before):
    return PriorityQueue(empty_list(), comes_before)

# PQueue, value -> PQueue
# adds the value to the queue(in the appropriate position)
def enqueue(pqueue, value):
    pqueue.list = insert_sorted(pqueue.list, value, pqueue.comes_before)
    return pqueue

def insert_sorted(list, value, comes_before):
    if list == None:
        return Pair(value, None)
    elif (comes_before(value, list.first)):
        return Pair(value, list)
    else:
        return Pair(list.first, insert_sorted(list.rest, value, comes_before))

# PQueue -> (value, PQueue)
# removes the element previously at the beginning of the PQueue and the new PQueue
def dequeue(pqueue):
    if pqueue.list == None:
        raise IndexError
    else:
        val, pqueue.list =  remove(pqueue.list, 0)
        return val, pqueue

# PQueue -> value
# returns the value at the beginning of the queue
def peek(pqueue):
    if pqueue.list == None:
        raise IndexError
    else:
        return pqueue.list.first

# PQueue -> int
# returns the number of elements in the PQueue
def size(pqueue):
    if pqueue.list == None:
        return 0
    else:
        return length(pqueue.list)

# PQueue -> boolean
# returns True if the queue is empty. Else False
def is_empty(pqueue):
    if length(pqueue.list) == 0:
        return True
    else:
        return False

class Pair:
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest

    def __eq__(self, other):
        return (type(other) == Pair
                and self.first == other.first
                and self.rest == other.rest
                )

    def __repr__(self):
        return "Pair(%r, %r)" % (self.first, self.rest)

# no args -> list
# returns an empty list.
def empty_list():
    return None

# list, int, value -> list
# adds an element to a specified position in a linked list
def add(list, index, value):
    if list == None and index != 0:
        raise IndexError
    elif index == 0:
        return Pair(value, None)
    else:
        return Pair(list.first, add(list.rest, index - 1, value))

# list -> int
# returns the length of the linked list
def length(list):
    if list == None:
        return 0
    else:
        return 1 + length(list.rest)

# list, int -> value
# returns the value at a specified index of a linked list
def get(list, index, counter = 0):
    if index < 0 or list == None:
        raise IndexError
    else:
        if index == counter:
            return list.first
        else:
            return get(list, index, counter + 1)

# list, int -> (value, list)
# Removes an element from a linked list and returns a tuple of the removed value and the new list
def remove(list, index):
    if index < 0 or list == None:
        raise IndexError
    else:
        return (get(list, index), get_list_remove(list, index))

# list, int -> list
# returns the list with the element at a specified index
def get_list_remove(list, index, counter = 0):
    if index == counter:
        return list.rest
    else:
        return Pair(list.first, get_list_remove(list.rest, index, counter + 1))