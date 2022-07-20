# 栈的实现

class Stack(object):
    """栈"""
    def __init__(self) -> None:
        self.__data = []

    def push(self, data):
        """压栈"""
        self.__data += [data]

    def pop(self):
        """出栈"""
        return self.__data.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.__data:
            return self.__data[-1]
        else:
            return None

    def is_empty(self):
        """判断栈是否为空"""
        return self.length == 0

    def length(self):
        """返回栈的长度"""
        return len(self.__data)


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.is_empty())
    print(s.length())
    print(s.peek())
    print(s.pop())
    print(s.pop())
    print(s.pop())
