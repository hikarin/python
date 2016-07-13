class Queue:
    class Cell:
        def __init__(self, x, y = None):
            self.data = x
            self.next = y

    def __init__(self):
        self.size = 0
        self.top = None
        self.rear = None

    def enqueue(self, data):
        new_cell = Queue.Cell(data, None)

        if self.size == 0:
            self.top = new_cell
            self.rear = new_cell
            self.size = 1
        else:
            new_cell.next = None
            self.rear.next = new_cell
            self.rear = new_cell
            self.size += 1
    
    def dequeue(self):
        if self.size <= 0:
            raise IndexError
        front = self.top
        self.top = self.top.next
        self.size -= 1
        return front.data

    def isEmpty(self):
        return (self.size == 0)

    def __str__(self):
        if self.size == 0:
            return 'Queue()'
        cp = self.peek()
        n = self.size
        _str = 'Queue('
        while n > 1:
            _str += '%d,' % cp.data
            cp = cp.next
            n -= 1
        _str += '%s)' % cp.data
        return _str

    def peek(self):
        return self.top


if __name__ == '__main__':
    q = Queue()
    print q.isEmpty()
    for x in range(5): q.enqueue(x)
    print q
    while not q.isEmpty():
        print q.dequeue(),
        print q
    print q

