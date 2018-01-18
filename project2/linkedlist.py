# a linked list is one of
# None, or
# an object Pair

class Pair:
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest

    def __eq__(self, other):
        return ((type(other) == Pair)
                and self.first == other.first
                and self.rest == other.rest
                )

    def __repr__(self):
        return ("Pair({!r}, {!r})".format(self.value, self.rest))

# no arguments -> None
# takes in 0 arguments, and returns an empty list
def empty_list():
    return None

# list int value -> list
# puts the value at the index specified in your list
def add(llist, index, value, counter = 0):
    if (index < 0 or index > length(llist)):
        raise IndexError
    elif (counter == index):
        return Pair(value, llist)
    else:
        return Pair(llist.first, add(llist.rest, index, value, counter + 1))

# list -> int
# returns the number of elements in your lsit
def length(llist):
    if (llist == None):
        return 0
    else:
        return 1 + length(llist.rest)

# list int -> value
# returns the value at the index position in the list
def get(llist, index, counter = 0):
    if (index < 0 or index > length(llist)):
        raise IndexError
    else:
        if (index == counter):
            return llist.first
        else:
            return get(llist.rest, index, counter + 1)

# list int value -> list
# replaces the element at the index position with the given value.
def set(llist, index, value, counter = 0):
    if (index < 0 or index > length(llist)):
        raise IndexError
    elif counter == index:
        if counter == length(llist) + counter:
            return Pair(value, None)
        else:
            return Pair(value, llist.rest)
    else:
        return Pair(llist.first, set(llist.rest, index, value, counter + 1))

# list int -> list
# removes the element at the given index of the list
def removing(llist, index, counter = 0):
    if (index < 0 or index > length(llist)):
        raise IndexError
    elif (counter == index):
        return llist.rest
    else:
        return Pair(llist.first, removing(llist.rest, index, counter + 1))

# list int -> tuple
# returns a 2-tuple with {element before(removed element} and the resulting list.
def remove(llist, index):
    if (index < 0 or index > length(llist)):
        raise IndexError
    else:
        return (get(llist, index), removing(llist, index))

# list function -> Nothing
# allows us to access each element in our linked list
def foreach(alist, function):
    if (alist is not None):
        function(list.first)
        foreach(list.rest, function)