import unittest
from main import Stack

class TestStack(unittest.TestCase):
    def test_push_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
    def test_peek(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.peek(), 2)
    def test_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push(10)
        self.assertFalse(stack.is_empty())
        stack.pop()
        self.assertTrue(stack.is_empty())
        stack.push('Python')
        self.assertFalse(stack.is_empty())

if __name__ == '__main__':
    unittest.main()
