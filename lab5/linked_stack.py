from linked_list import *

# A Stack is one of
# None, or
# Pair(value, Stack)

# no args -> Stack
# returns an empty Stack
def empty_stack():
    return empty_list()

# Stack any -> Stack
# Pushes a value to a stack
def push(stack, value):
    return add(stack, 0, value)

# Stack -> (any, Stack)
# Pops and returns resulting stack
def pop(stack):
    if stack == None:
        raise IndexError
    else:
        return remove(stack, 0)

# Stack -> value
# returns the top element of a stack
def peek(stack):
    if stack == None:
        raise IndexError
    else:
        return get(stack, 0)

# Stack -> int
# returns size of a stack
def size(stack):
    return length(stack)

# Stack -> boolean
# determines whether or not a stack is empty
def is_empty(stack):
    return stack == None