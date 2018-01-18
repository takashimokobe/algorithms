import unittest
from circular_queue import *


class TestQueue(unittest.TestCase):
    def test00_interface(self):
        test_queue = empty_queue()
        test_queue = enqueue(test_queue, "foo")
        peek(test_queue)
        _, test_queue = dequeue(test_queue)
        size(test_queue)
        is_empty(test_queue)

    def test_repr(self):
        self.assertEqual(repr(empty_queue()), "Queue(%r, 0, 0, 0)" % ([None] * 5000))

    def test_empty(self):
        self.assertEqual(empty_queue(), Queue([None] * 5000, 0, 0, 0))

    def test_enqueue(self):
        q = empty_queue()
        queued_item = [5]
        queued_item.extend([None] * 4999)

        self.assertEqual(enqueue(q, 5), Queue(queued_item, 1, 0, 1))

    def test_enq_error(self):
        q = empty_queue()
        for i in range(5000):
            q = enqueue(q, random.randrange(10000))

        self.assertRaises(IndexError, enqueue, q, 5)

    def test_dequeue(self):
        q = empty_queue()
        q1 = enqueue(q, 4)
        q2 = enqueue(q1, 5)
        new_queue = [4, 5]
        new_queue.extend([None] * 4998)
        self.assertEqual(dequeue(q2), (4, Queue(new_queue, 1, 1, 2)))

    def test_dq_error(self):
        q = empty_queue()
        q1 = enqueue(q, 4)
        q2 = enqueue(q1, 2)
        q3 = dequeue(q2)
        q4 = dequeue(q3[1])
        self.assertRaises(IndexError, dequeue, q4[1])

    def test_peek(self):
        q = empty_queue()
        q1 = enqueue(q, 4)
        q2 = enqueue(q, 2)
        self.assertEqual(peek(q2), 4)

    def test_peek_error(self):
        q = empty_queue()
        self.assertRaises(IndexError, peek, q)

    def test_size(self):
        q = empty_queue()
        q1 = enqueue(q, 2)
        q2 = dequeue(q1)
        self.assertEqual(size(q2[1]), 0)

    def test_is_empty(self):
        q = empty_queue()
        self.assertTrue(is_empty(q))

if __name__ == "__main__":
    unittest.main()


