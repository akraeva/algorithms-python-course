# Stepick.org — Алгоритмы в Python — просто, наглядно, с нуля!
# 2. Структуры данных и их алгоритмы


# 2.1 Массивы и списки: отличие, вставка, удаление


def m_2_1_4():
    class Array:

        def __init__(self, size):
            self.size = size
            self.data = [None] * size

        def insert(self, index, value):
            if not (0 <= index < self.size):
                raise IndexError("Index out of range")
            self.data[index] = value


def m_2_1_2():
    class Array:
        def __init__(self, size):
            self.data = [None] * size

        def insert(self, index, value):
            if 0 <= index < len(self.data):
                self.data[index] = value
            else:
                raise IndexError("Index out of bounds")

        def delete(self, index):
            if not (0 <= index < len(self.data)):
                raise IndexError("Index out of bounds")
            self.data[index] = None


def m_2_1_3():
    class Array:
        def __init__(self, size):
            self.data = [None] * size

        def insert(self, index, value):
            if 0 <= index < len(self.data):
                self.data[index] = value
            else:
                raise IndexError("Index out of bounds")

        def get(self, index):
            if 0 <= index < len(self.data):
                return self.data[index]
            else:
                raise IndexError("Index out of bounds")


def m_2_1_4():
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class SinglyLinkedList:
        def __init__(self):
            self.head = None

        def append(self, data):
            new_node = Node(data)
            if not self.head:
                self.head = new_node
                return
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        def print_list(self):
            current = self.head
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")


def m_2_1_5():
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class SinglyLinkedList:
        def __init__(self):
            self.head = None

        def append(self, data):
            new_node = Node(data)
            if not self.head:
                self.head = new_node
                return
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        def find(self, value):
            current = self.head
            while current.next:
                if current.data == value:
                    return True
                current = current.next
            return False


# 2.2 Стек и очередь: принципы и реализация


def m_2_2_1():
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class MyStack:
        def __init__(self):
            self.top = None

        def push(self, value):
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node

        def pop(self):
            value = self.top.data
            self.top = self.top.next
            return value

        def peek(self):
            if self.is_empty():
                return None
            return self.top.data

        def is_empty(self):
            return self.top is None


def m_2_2_2():
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class MyQueue:
        def __init__(self):
            self.front = None  # первый элемент
            self.rear = None  # последний элемент

        def enqueue(self, value):
            new_node = Node(value)
            if self.rear is None:
                self.front = new_node
                self.rear = new_node
            else:
                self.rear.next = new_node
                self.rear = new_node

        def dequeue(self):
            if self.front is None:
                return None
            value = self.front
            self.front = value.next
            if self.front is None:
                self.rear = None
            return value.data

        def peek(self):
            if self.front:
                return self.front.data
            else:
                return None

        def is_empty(self):
            return self.front is None


def m_2_2_3():
    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

    class MyDeque:
        def __init__(self):
            self.head = None  # начало очереди (слева)
            self.tail = None  # конец очереди (справа)

        def append_left(self, value):
            new_node = Node(value)
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self.tail is None:
                self.tail = new_node

        def append_right(self, value):
            new_node = Node(value)
            new_node.prev = self.tail
            if self.tail:
                self.tail.next = new_node
            self.tail = new_node
            if self.head is None:
                self.head = new_node

        def pop_left(self):
            if self.head is None:
                return None
            value = self.head.data
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None
            return value

        def pop_right(self):
            if self.tail is None:
                return None
            value = self.tail.data
            self.tail = self.tail.prev
            if self.tail is not None:
                self.tail.next = None
            else:
                self.head = None
            return value


def m_2_2_4():
    class PriorityQueue:
        def __init__(self):
            self.items = []

        def enqueue(self, value, priority):
            self.items.append((value, priority))

        def dequeue(self):
            if not self.items:
                raise IndexError("Очередь пуста")
            item = min(self.items, key=lambda x: x[1])
            value = self.items.pop(self.items.index(item))
            return value[0]

        def is_empty(self):
            return not self.items


def m_2_2_5():
    class BrowserHistory:
        def __init__(self):
            self.history = []
            self.current_url = None

        def visit(self, url):
            if self.current_url:
                self.history.append(self.current_url)
            self.current_url = url

        def back(self):
            if self.history:
                self.current_url = self.history.pop()
                return self.current_url
            else:
                raise IndexError("История пуста")

        def current(self):
            return self.current_url


# 2.3 Хэш-таблица и разрешение коллизий


def m_2_3_1():
    def weighted_hash(key, size):
        hash = sum(ord(ch) * (i + 1) for i, ch in enumerate(key)) % size
        return hash


def m_2_3_2():
    class SimpleHashTable:
        def __init__(self, size):
            self.size = size
            self.table = [None] * size

        def _hash(self, key):
            return sum(ord(c) for c in key) % self.size

        def insert(self, key, value):
            index = self._hash(key)
            if not self.table[index]:
                self.table[index] = (key, value)
            elif self.table[index][0] == key:
                self.table[index] = (key, value)

        def get(self, key):
            index = self._hash(key)
            if self.table[index] and self.table[index][0] == key:
                return self.table[index][1]
            return None


def m_2_3_3():
    class HashTable:
        def __init__(self, size=10):
            self.size = size
            self.table = [[] for _ in range(size)]

        def _hash(self, key):
            return sum(ord(c) for c in key) % self.size

        def insert(self, key, value):
            index = self._hash(key)
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, value)
                    return
            self.table[index].append((key, value))

        def get(self, key):
            index = self._hash(key)
            for k, v in self.table[index]:
                if k == key:
                    return v
            return None
