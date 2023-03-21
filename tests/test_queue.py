"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src import queue


class TestStak(unittest.TestCase):

    def test_enqueue(self):
        test_queue = queue.Queue()
        test_queue.enqueue('data1')
        test_queue.enqueue('data2')
        self.assertEqual(test_queue.head.data, 'data1')
        self.assertEqual(test_queue.head.next_node, 'data2')

    def test_dequeue(self):
        test_queue = queue.Queue()
        test_queue.enqueue('data1')
        test_queue.dequeue()
        with self.assertRaises(AttributeError):
            test_queue.head.data

    def test_str_for_queue(self):
        test_queue = queue.Queue()
        test_queue.enqueue('data1')
        test_queue.enqueue('data2')
        self.assertEqual(str(test_queue), "data2\ndata2")

