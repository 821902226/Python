# 队列（Python实现）

class Queue(object):
    """队列"""
    def __init__(self) -> None:
        self.__data = []

    def enqueue(self, data):
        """进队"""
        self.__data += [data]

    def dequeue(self):
        """出队"""
        return self.__data.pop(0)

    def is_empty(self):
        """队列是否为空"""
        return self.length() == 0

    def length(self):
        """队列的长度"""
        return len(self.__data)


if __name__ == "__main__":
    q = Queue()
    print(q.is_empty())
    q.enqueue(1)
    q.enqueue(3)
    q.enqueue(5)
    print(q.length())
    print(q.is_empty())
    q.dequeue()
    q.dequeue()
    q.dequeue()
    print(q.length())
    print(q.is_empty())
