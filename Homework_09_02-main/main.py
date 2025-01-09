from QueueClass import Queue

def main():
    size = int(input("Введите размер очереди: "))
    queue = Queue(size)

    while True:
        print("\nМеню:")
        print("1. Добавить элемент в очередь (Enqueue)")
        print("2. Удалить элемент из очереди (Dequeue)")
        print("3. Проверить, пуста ли очередь (IsEmpty)")
        print("4. Проверить, полна ли очередь (IsFull)")
        print("5. Показать все элементы очереди (Show)")
        print("6. Выход")

        choice = input("Выберите операцию: ")

        if choice == '1':
            item = input("Введите элемент для добавления: ")
            try:
                queue.enqueue(item)
                print(f"Элемент '{item}' добавлен в очередь.")
            except Exception as e:
                print(e)

        elif choice == '2':
            try:
                removed_item = queue.dequeue()
                print(f"Элемент '{removed_item}' удален из очереди.")
            except Exception as e:
                print(e)

        elif choice == '3':
            if queue.is_empty():
                print("Очередь пуста.")
            else:
                print("Очередь не пуста.")

        elif choice == '4':
            if queue.is_full():
                print("Очередь полна.")
            else:
                print("Очередь не полна.")

        elif choice == '5':
            print("Элементы очереди:", queue.show())

        elif choice == '6':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
