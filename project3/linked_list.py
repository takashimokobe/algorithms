# Section 1: LinkedList

# AnyList Data Definition

# an AnyList is one of the following
# - None, or
# - Pair(first, rest)

class Pair:
    def __init__(self, first, rest):
        self.first = first              # the first value in the linked list
        self.rest = rest                # the rest of the values in the linked list

    def __eq__(self, other):
        return (type(other) == Pair
                and self.first == other.first
                and self.rest == other.rest)

    def __repr__(self):
        return ("%r, %r" % (self.first, self.rest))


# Functions

# No arguments
# Returns an empty list

def empty_list():
    return None


# AnyList int [any type] -> AnyList
# Returns a new list with the given value inserted at the given index

def add(list, index, value):
    if (list == None and index == 0):       # if the list is None and the index is 0
        return Pair(value, None)            # return Pair(value, None)
    if (list == None):                      # if the list is None, at all,
        raise IndexError("Index is out of bounds")  # raise an index error
    if (index == 0):                        # if the index is 0
        return Pair(value, list)            # return a pair with the index at 0
    if (list.rest == None and index > 1):   # if the rest of the list is None and the index is greater than 1
        raise IndexError("Index is out of bounds")  # raise an indexerror
    return Pair(list.first, add(list.rest, index - 1, value)) # return a pair with the first value, and using add on the rest of the list to find the correct index


# AnyList -> int
# Returns number of elements in list

def length(list):
    if (list == None):                      # if the list == None
        return 0                            # return 0
    return 1 + length(list.rest)            # return the length of the list


# AnyList int -> int
# Returns value at given index

def get(list, index):
    if (list == None):                              # if list is none
        raise IndexError("Index is out of bounds")  # raise an index error
    if (list.rest == None and index > 0):           # if the list of the list is None, and the index is greater than 0
        raise IndexError("Index is out of bounds")  # raise index out of bounds error
    if (index == 0):                                # if the index is 0
        return list.first                           # return the first value of the pair
    return get(list.rest, index - 1)                # call get recursively while making the list shorter. decrement index

# AnyList int [any type] -> AnyList
# Returns list with element replaced with given value at given index
def set(list, index, value):
    if (list == None):
        raise IndexError("Index is out of bounds")
    if (list.rest == None and index > 0):
        raise IndexError("Index is out of bounds")
    if (index == 0):                                                # if the index is 0
        return Pair(value, list.rest)                               # return a Pair with the value at the 0 index, and the rest of the list
    return Pair(list.first, set(list.rest, index - 1, value))       # else return a pair with the first value, and call set recursively on the rest of the list. decrement index

# AnyList int -> Tuple
# Returns 2-tuple of removed element and resulting list
def remove(list, index):
    if (list == None):
        raise IndexError("Index is out of bounds")
    if (list.rest == None and index > 0):
        raise IndexError("Index is out of bounds")
    return remove_element(list, index), remove_list(list, index)           # return a tuple of the removed element, and the list after the remove is done

# AnyList int -> AnyList
# Returns list with removed element at given index
def remove_list(list, index):
    if (list == None):
        raise IndexError("Index is out of bounds")
    if (list.rest == None and index > 0):
        raise IndexError("Index is out of bounds")
    if (index == 0):                                                       # if the list is 0, return the rest of the list. This removes teh value at the first index
        return list.rest
    return Pair(list.first, remove_list(list.rest, index - 1))             # else, return Pair with the first value, then call remove recursively on the rest of your list. decrement your counter


# AnyList int -> [any value]
# Returns removed element at given index
def remove_element(list, index):
    if (list == None):
        raise IndexError("Index is out of bounds")
    if (list.rest == None and index > 0):
        raise IndexError("Index is out of bounds")
    if (index == 0):
        return list.first                                                  # if your index is 0, return the first element in your Pair
    return remove_element(list.rest, index - 1)                            # else, called remove_element recursively on the rest of your list, decrement counter. until you find the element at the index specified

# list function -> Nothing
# allows us to access each element in our linked list
def foreach(llist, function):
    if (llist is not None):                                                # if your linked_list is not none
        function(llist.first)                                              # call the function on the first value of your linkedlist
        foreach(llist.rest, function)                                      # call foreach recursively to the rest of your list, a function.

# list lessthan -> list
# sorts your list in descending order
def insert_sorted(llist, value, comes_before):
    if (llist == None):
        return Pair(value, None)
    else:
        if comes_before(value, llist.first):
            return Pair(value, llist)
        else:
            return Pair(llist.first, insert_sorted(llist.rest, value, comes_before))
