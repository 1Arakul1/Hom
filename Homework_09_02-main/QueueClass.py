class Queue:
    """Класс для представления очереди."""

    def __init__(self, size):
        """
        Инициализация очереди.

        :param size: Максимальный размер очереди.
        """
        self.size = size
        self.queue = []

    def is_empty(self):
        """Проверка очереди на пустоту."""
        return len(self.queue) == 0

    def is_full(self):
        """Проверка очереди на заполнение."""
        return len(self.queue) == self.size

    def enqueue(self, item):
        """
        Добавление элемента в очередь.

        :param item: Элемент для добавления.
        :raises Exception: Если очередь полна.
        """
        if self.is_full():
            raise Exception("Очередь полна")
        self.queue.append(item)

    def dequeue(self):
        """
        Удаление элемента из очереди.

        :raises Exception: Если очередь пуста.
        :return: Удаленный элемент.
        """
        if self.is_empty():
            raise Exception("Очередь пуста")
        return self.queue.pop(0)

    def show(self):
        """Отображение всех элементов очереди."""
        return self.queue