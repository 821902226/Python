# 单向链表

class Node(object):
    """节点"""
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkList(object):
    """单链表"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表的长度"""
        cur = self.__head
        length = 0
        while cur is not None:
            cur = cur.next
            length += 1
        return length

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.next
        print('')

    def add(self, item):
        """首部添加元素"""
        node = Node(data=item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """尾部添加元素"""
        node = Node(data=item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, index, item):
        """指定位置添加元素"""
        if index <= 0:
            self.add(item)
        elif index >= self.length():
            self.append(item)
        else:
            node = Node(data=item)
            cur = self.__head
            count = 0
            while count < index-1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除指定节点"""
        while self.__head.data == item:
            self.__head = self.__head.next
        cur = self.__head
        while cur.next is not None:
            if cur.next.data == item:
                cur.next = cur.next.next
                if cur.next is None:
                    break
            cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.data == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':

    ll = SingleLinkList()

    print(ll.is_empty())

    for i in range(5):
        ll.append(i+1)

    ll.add(0)

    print(ll.is_empty())
    print(ll.length())

    print(ll.search(5))

    ll.insert(3, 9)
    ll.insert(-1, 100)
    ll.insert(-1, 100)
    ll.insert(10, 200)
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(4)
    ll.travel()
    ll.remove(200)
    ll.travel()
