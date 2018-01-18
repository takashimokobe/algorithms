from priority_queue import *
from time import *
# An Event Queue is one of
# None, or
# PriorityQueue(list, comes_before)

class EventQueue:
    def __init__(self):
        self.pqueue = empty_pqueue(event_before)
        self.time = 0

    def __eq__(self, other):
        return ((type(other) == EventQueue)
          and self.pqueue == other.pqueue
          and self.time == other.time
        )

    def __repr__(self):
        return ("EventQueue({!r}, {!r})".format(self.pqueue, self.time))

# an event is an element of event queue
class Event:
    def __init__(self, func, time):
        self.func = func
        self.time = time

    def __eq__(self, other):
        return (type(other) == Event
                and self.func == other.func
                and self.time == other.time
                )

    def __repr__(self):
        return ("Event({!r}, {!r})".format(self.func, self.time))

# EventQueue, EventQueue -> boolean
# checks that the time of an Event is before the time of the EventQueue
def event_before(equeue, equeue2):
    return equeue.time > equeue2.time

# EventQueue, function , time -> EventQueue
# stores the event to be scheduled in the EventQueue
def add_event(equeue, func, after):
    equeue.pqueue = enqueue(equeue.pqueue, Event(func, equeue.time + after))
    return equeue

# EventQueue -> void
# runs each elemet in your PriorityQueue
def run_events(equeue):
    while (equeue.pqueue is not None):
        a, equeue.pqueue = dequeue(equeue.pqueue)
        if a.time != equeue.time:
            equeue.time = a.time
        a.func(equeue)