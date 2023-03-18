"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack


class TestStack(unittest.TestCase):
    test_stack = Stack()

    def test_push(self):
        self.test_stack.push('test')
        self.assertEqual(self.test_stack, self.test_stack)

    def test_pop(self):
        self.test_stack.push('data1')
        data = self.test_stack.pop()
        self.assertEqual(data, 'data1')




