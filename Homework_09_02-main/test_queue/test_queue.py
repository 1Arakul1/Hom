import unittest
from QueueClass import Queue

class TestQueue(unittest.TestCase):

    def setUp(self):
        """Создаем новую очередь для тестов."""
        self.queue = Queue(3)

    def test_is_empty(self):
        """Тестируем проверку очереди на пустоту."""
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue('A')
        self.assertFalse(self.queue.is_empty())

    def test_is_full(self):
        """Тестируем проверку очереди на заполнение."""
        self.queue.enqueue('A')
        self.queue.enqueue('B')
        self.queue.enqueue('C')
        self.assertTrue(self.queue.is_full())
        self.queue.dequeue()
        self.assertFalse(self.queue.is_full())

if __name__ == '__main__':
    unittest.main()
