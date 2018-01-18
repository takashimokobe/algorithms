import unittest
from list_queue import *

class TestQueue(unittest.TestCase):
    def test00_interface(self):
        test_queue = empty_queue()
        test_queue = enqueue(test_queue, "foo")
        peek(test_queue)
        _, test_queue = dequeue(test_queue)
        size(test_queue)
        is_empty(test_queue)

    def test_repr(self):

        q = empty_queue()
        self.assertEqual(repr(q), "Front: None, Back: None")

    def test_empty(self):

        self.assertEqual(empty_queue(), Queue(None, None))

    def test_enq(self):

        early = Pair(5, Pair(4, None))
        late = Pair(1, None)
        self.assertEqual(enqueue(Queue(early, late), 5), Queue(Pair(5, Pair(4, None)), Pair(5, Pair(1, None))))


    def test_reverse(self):

        lst1 = Pair(1, Pair(2, Pair(5, None)))
        self.assertEqual(reverse(lst1), Pair(5, Pair(2, Pair(1, None))))

    def test_dequeue(self):

        q = empty_queue()
        q1 = enqueue(q, 2)
        q2 = enqueue(q1, 3)
        self.assertEqual(dequeue(q2), (2, Queue(Pair(3, None), None)))

    def test_dequeue2(self):

        q = empty_queue()
        q1 = enqueue(q, 2)
        q2 = enqueue(q1, 3)
        q3 = dequeue(q2)
        self.assertEqual(dequeue(q3[1]), (3, Queue(None, None)))


    def test_dq_error(self):

        q = empty_queue()
        self.assertRaises(IndexError, dequeue, q)

    def test_peek(self):

        q = empty_queue()
        q1 = enqueue(q, 5)
        q2 = enqueue(q1, 7)
        self.assertEqual(peek(q2), 5)

    def test_peek2(self):

        q = empty_queue()
        q1 = enqueue(q, 2)
        q2 = enqueue(q1, 3)
        q3 = dequeue(q2)
        self.assertEqual(peek(q3[1]), 3)

    def test_peek_error(self):

        q = empty_queue()
        self.assertRaises(IndexError, peek, q)

    def test_size(self):

        q = empty_queue()
        q1 = enqueue(q, 1)
        q2 = enqueue(q1, 6)
        q3 = dequeue(q2)
        q4 = enqueue(q3[1], 4)
        self.assertEqual(size(q4), 2)

    def test_is_empty(self):

        q = empty_queue()
        q1 = enqueue(q, 5)
        self.assertFalse(is_empty(q1))

if __name__ == "__main__":
	unittest.main()
