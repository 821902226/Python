# 二叉树算法

class Node(object):
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self) -> None:
        self.root = None

    def add(self, data):
        """添加数据"""
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            queue = [self.root]
            while True:
                cur_node = queue.pop(0)
                if cur_node.left is None:
                    cur_node.left = node
                    break
                else:
                    queue.append(cur_node.left)
                if cur_node.right is None:
                    cur_node.right = node
                    break
                else:
                    queue.append(cur_node.right)

    def travel(self):
        """广度遍历"""
        if self.root is None:
            print(None)
        else:
            queue = [self.root]
            while queue:
                cur_node = queue.pop(0)
                print(cur_node.data, end=' ')
                if cur_node.left is not None:
                    queue.append(cur_node.left)
                if cur_node.right is not None:
                    queue.append(cur_node.right)
            print('')

    def preorder(self, root):
        """先序遍历"""
        if root is None:
            return
        print(root.data, end=' ')
        self.preorder(root.left)
        self.preorder(root.right)
    
    def midorder(self, root):
        """中序遍历"""
        if root is None:
            return
        self.midorder(root.left)
        print(root.data, end=' ')
        self.midorder(root.right)

    def endorder(self, root):
        """后序遍历"""
        if root is None:
            return
        self.endorder(root.left)
        self.endorder(root.right)
        print(root.data, end=' ')


if __name__ == "__main__":
    tree = Tree()

    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.travel()
    tree.preorder(tree.root)
    print('')
    tree.midorder(tree.root)
    print('')
    tree.endorder(tree.root)
    print('')
