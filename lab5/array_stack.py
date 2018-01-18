from array_list import *

# Stack is an arrayList where one of:
# List([], 0)
# List([])

# no args -> Stack
# Returns an empty stack.
def empty_stack():
    return empty_list()

# Stack any -> Stack
# pushes a specified value to a stack
def push(stack, value):
    return add(stack, length(stack), value)

# Stack -> (any, Stack)
# removes teh top element of a stack
def pop(stack):
    if stack.list == []:
        raise IndexError
    else:
        return remove(stack, length(stack)- 1)

# Stack -> any
# returns the top element of a stack
def peek(stack):
    if stack.list == []:
        raise IndexError
    else:
        return stack.list[length(stack) - 1]

# Stack -> int
# Returns the size of a stack
def size(stack):
    return length(stack)

# Stack -> boolean
# Determines whether or not a stack is empty
def is_empty(stack):
    return length(stack) == 0

