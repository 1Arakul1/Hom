import unittest
from LinkedListClass import LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        """Создаем новый связный список для тестов."""
        self.ll = LinkedList()

    def test_insert_at_head(self):
        """Тестируем вставку узла в начало списка."""
        self.assertEqual(self.ll.insert_at_head(10), "Узел с данными 10 добавлен в начало списка")
        self.assertEqual(self.ll.head.data, 10)

    def test_insert_at_end(self):
        """Тестируем вставку узла в конец списка."""
        self.ll.insert_at_head(10)
        self.assertEqual(self.ll.insert_at_end(20), "Узел с данными 20 добавлен в конец списка")
        self.assertEqual(self.ll.head.next_node.data, 20)

    def test_remove_node_position(self):
        """Тестируем удаление узла по позиции."""
        self.ll.insert_at_head(10)
        self.ll.insert_at_end(20)
        self.assertEqual(self.ll.remove_node_position(1), "Удален узел с данными 10 позиции 1")
        self.assertEqual(self.ll.head.data, 20)

    def test_change_data(self):
        """Тестируем изменение данных в узле."""
        self.ll.insert_at_head(10)
        self.assertEqual(self.ll.change_data(10, 15), "Заменены данные в узле № 1")
        self.assertEqual(self.ll.head.data, 15)

if __name__ == '__main__':
    unittest.main()
