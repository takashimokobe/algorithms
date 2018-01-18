import unittest


# An AnyList is one of:
# - None or
# - Pair(first, rest)

# Represents a linked list.
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


# -> AnyList
# Returns an empty list.

def empty_list():
    return None


# AnyList int any -> AnyList
# Adds an element to a specified position in a linked list.

def add(lst, index, value):
    if lst == None and index != 0:
        raise IndexError
    elif index == 0:
        return Pair(value, lst)
    else:
        return Pair(lst.first, add(lst.rest, index - 1, value))


# AnyList -> int
# Returns the length of the linked list.
def length(anyList):
    if anyList == None:

        return 0

    else:

        return 1 + length(anyList.rest)


# AnyList int -> any
# Returns the value at a specific index of a linked list.
def get(anyList, index, anyListIndex=0):
    if index < 0 or anyList == None:

        raise IndexError()

    else:

        if anyListIndex == index:

            return anyList.first

        else:

            return get(anyList.rest, index, anyListIndex + 1)


# AnyList int any -> AnyList
# Replaces the value at a specific index in a linked list.
def set(anyList, index, value, anyListIndex=0):
    if (index < 0 or anyList == None):

        raise IndexError()

    else:

        if anyListIndex == index:

            return Pair(value, anyList.rest)

        else:

            return Pair(anyList.first, set(anyList.rest, index, value, anyListIndex + 1))


# AnyList int -> (any, AnyList)
# Removes an element from a linked list and returns a tuple of the removed value and resulting list.

def remove(anyList, index):
    if index < 0 or anyList == None:

        raise IndexError()

    else:

        return (get(anyList, index), get_list_remove(anyList, index))


# AnyList int -> AnyList
# Returns the linked list with the element at a specific index removed.

def get_list_remove(anyList, index, anyListIndex=0):
    if anyListIndex == index:

        return anyList.rest

    else:

        return Pair(anyList.first, get_list_remove(anyList.rest, index, anyListIndex + 1))


def foreach(lst, func):
    if lst == None:
        return None
    else:
        func(lst.first)
        return foreach(lst.rest, func)


def sort(lst, func):
    if lst == None:
        return None
    else:
        return helpersup(sort(lst.rest, func), lst.first, func)


def helpersup(newlst, value, func):
    if newlst == None:
        return Pair(value, None)
    elif func(value, newlst.first):
        return Pair(value, newlst)
    else:
        return Pair(newlst.first, helpersup(newlst.rest, value, func))





