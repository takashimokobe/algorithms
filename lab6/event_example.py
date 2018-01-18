from event_queue import * 
import sys

def comes_before(x, y):
	return x < y

def print_each_second(equeue):
	print('\ttime {}: every one'.format(equeue.time))
	return add_event(equeue, print_each_second, 1)

def print_every_5_seconds(equeue):
	print('\ttime {}: every five'.format(equeue.time))
	return add_event(equeue, print_every_5_seconds, 5)

def print_at_15(equeue):
	print('\ttime {}: at fifteen'.format(equeue.time))

def stop(equeue):
	print('\ttime {}: stopping'.format(equeue.time))
	sys.ext(0)

if __name__ == '__main__':
    equeue = EventQueue()

    add_event(equeue, stop, 20)
    add_event(equeue, print_at_15, 15)
    add_event(equeue, print_every_5_seconds, 5)
    add_event(equeue, print_each_second, 1)

    run_events(equeue)