class Jar:
    def __init__(self, capacity=12):
        self._size = 0
        self.capacity = capacity

    def __str__(self):
        return self._size * "🍪"

    def withdraw(self, n):
        self.size -= n

    def deposit(self, n):
        self.size += n


    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, n):
        if n < 0:
            raise ValueError()
        self._capacity = n

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        if n > self._capacity:
            raise ValueError()
        elif n < 0:
            raise ValueError()
        self._size = n