import unittest
from priority_queue import *

def comes_before(x, y):
    return x < y

class TestCase(unittest.TestCase):

    def test00_interface(self):
        test_pqueue = empty_pqueue(comes_before)
        test_pqueue = enqueue(test_pqueue, 3)
        peek(test_pqueue)
        _, test_pqueue = dequeue(test_pqueue)
        size(test_pqueue)
        is_empty(test_pqueue)

    def test_empty_pqeue(self):
        self.assertEqual(empty_pqueue(comes_before), PriorityQueue(None, comes_before))

    def test_enqueue(self):
        pq = empty_pqueue(comes_before)
        pq = enqueue(pq, 1)
        pq = enqueue(pq, 3)
        pq = enqueue(pq, 10)
        pq = enqueue(pq, 4)
        self.assertEqual(pq, PriorityQueue(Pair(1, Pair(3, Pair(4, Pair(10, None)))), comes_before))

    def test_enqueue2(self):
        pq = PriorityQueue(Pair(1, Pair(3, Pair(5, None))), comes_before)
        self.assertEqual(enqueue(pq, 4), PriorityQueue(Pair(1, Pair(3, Pair(4, Pair(5, None)))), comes_before))

    def test_insert_sorted(self):
        list = Pair(1, Pair(4, Pair(10, None)))
        self.assertEqual(insert_sorted(list, 5, comes_before), Pair(1, Pair(4, Pair(5, Pair(10, None)))))

    def test_dequeue(self):
        pq = empty_pqueue(comes_before)
        print(pq)
        self.assertRaises(IndexError, dequeue, pq)

    def test_dequeue2(self):
        pq = PriorityQueue(Pair(1, Pair(3, Pair(5, None))), comes_before)
        self.assertEqual(dequeue(pq), (1, PriorityQueue(Pair(3, Pair(5, None)), comes_before)))

    def test_size(self):
        pq = empty_pqueue(comes_before)
        self.assertEqual(size(pq), 0)

    def test_size2(self):
        pq = PriorityQueue(Pair(1, Pair(4, None)), comes_before)
        self.assertEqual(size(pq), 2)

    def test_is_empty(self):
        pq = empty_pqueue(comes_before)
        self.assertTrue(is_empty(pq))

    def test_is_empty2(self):
        pq2 = PriorityQueue(Pair(1, Pair(3, Pair(5, None))), comes_before)
        self.assertFalse(is_empty(pq2))

    def test_empty_list(self):
        self.assertEqual(empty_list(), None)

    def test_add(self):
        list = Pair(1, Pair(4, Pair(10, None)))
        self.assertEqual(add(list, 1, 20), Pair(1, Pair(20, None)))

    def test_adder(self):
        list = Pair(1, Pair(4, Pair(10, None)))
        self.assertRaises(IndexError, add, list, -1, 200)

    def test_length(self):
        list = Pair(1, Pair(4, Pair(10, None)))
        self.assertEqual(length(list), 3)

    def test_length0(self):
        list = None
        self.assertEqual(length(list), 0)

    def test_get(self):
        list = Pair(1, Pair(3, Pair(4, Pair(10, None))))
        self.assertEqual(get(list, 1), 1)

    def test_geter(self):
        list = Pair(1, Pair(4, Pair(10, None)))
        self.assertRaises(IndexError, get, list, -1)

    def test_remove(self):
        list = Pair(1, Pair(3, Pair(4, Pair(10, None))))
        self.assertEqual(remove(list, 1), (1, Pair(1, Pair(4, Pair(10, None)))))

    def test_removeer(self):
        list = Pair(1, Pair(4, Pair(10, None)))
        self.assertRaises(IndexError, remove, list, -1)

    def test_get_list_remove(self):
        list = Pair(1, Pair(3, Pair(4, Pair(10, None))))
        self.assertEqual(get_list_remove(list, 1), Pair(1, Pair(4, Pair(10, None))))


if __name__=='__main__':
    unittest.main()