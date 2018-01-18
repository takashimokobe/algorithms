from linked_list import *

# A Queue is a Queue(anyList, anyList)
# where anyList is one of:
# None, or
# Pair(value, anyList)

class Queue:

	def __init__(self, early, late):

		self.early = early # An AnyList representing the front end of the queue (for dequeueing.)
		self.late = late # An AnyList representing the back end of the queue(for enqueueing.)

	def __eq__(self, other):

		return (type(other) == Queue
				and self.early == other.early
				and self.late == other.late
				)

	def __repr__(self):

		return "Front: %r, Back: %r" % (self.early, self.late)

# no args -> Queue
def empty_queue():
    return Queue(empty_list(), empty_list())

# Queue value -> Queue
# Enqueues a specified value.
def enqueue(queue, value):
    return Queue(queue.early, add(queue.late, 0, value))

# anyList -> anyList
# Reverses a linked list
def reverse(llist):
    new_list = empty_list()
    add_index = 0

    for i in range(length(llist), 0, -1):
        new_list = add(new_list, add_index, get(llist, i - 1))
        add_index += 1

    return new_list

# Queue -> (value, Queue)
# Dequeues the first element in a queue.
def dequeue(queue):
    if queue.early == None:
        if queue.late == None:
            raise IndexError()
        else:
            new_early = reverse(queue.late)
            return (new_early.first, Queue(new_early.rest, None))
    else:
        return (queue.early.first, Queue(queue.early.rest, queue.late))

# Queue -> value
# Returns the first item in a queue
def peek(queue):
    if queue.early == None:
        if queue.late == None:
            raise IndexError
        else:
            new_early = reverse(queue.late)
            return new_early.first
    else:
        return queue.early.first

# Queue -> int
# returns the size of a queue
def size(queue):
    return length(queue.early) + length(queue.late)

# Queue -> boolean
# Determines whether or not a queue is empty
def is_empty(queue):
    return queue.early == None and queue.late == None