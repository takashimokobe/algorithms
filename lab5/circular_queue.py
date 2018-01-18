import random

# A Queue is a Queue(list, size, start, end)

class Queue:
    def __init__(self, list, size = 0, start = 0, end = 0):
        self.list = list
        self.size = size
        self.start = start
        self.end = end

    def __eq__(self, other):
        return (type(other) == Queue
                and self.list == other.list
                and self.size == other.size
                and self.start == other.start
                and self.end == other.end
                )

    def __repr__(self):
        return "Queue(%r, %r, %r, %r)" % (self.list, self.size, self.start, self.end)

# no args -> Queue
# Returns an empty queue.
def empty_queue():
    return Queue([None] * 5000)

# Queue any -> Queue
# Adds a value to a queue.
def enqueue(queue, value):
    if queue.size < 5000:
        queue.list[queue.end] = value
        queue.size += 1
        queue.end = (queue.end + 1) % 5000
    else:
        raise IndexError
    return queue

# Queue -> (any, Queue)
# Removes the first item to come out of a queue
def dequeue(queue):
    if queue.size == 0:
        raise IndexError
    else:
        dequeued_value = queue.list[queue.start]
        queue.start = (queue.start + 1) % 5000
        queue.size -= 1
    return (dequeued_value, queue)

# Queue -> any
# Returns the first item to come out of a queue
def peek(queue):
    if queue.size == 0:
        raise IndexError
    else:
        return queue.list[queue.start]

# Queue -> int
# Returns the size of a queue
def size(queue):
    return queue.size

# Queue -> boolean
# Determines whether or not a queue is empty
def is_empty(queue):
    return (queue.size == 0)