from abc import ABC, abstractmethod


# 组合模式中的抽象组件类
class Node(ABC):
    def __init__(self, name):
        self.name = name

    # 抽象方法，具体实现由子类提供
    @abstractmethod
    def draw(self, icon_family, level=0, is_last=False):
        pass


# 容器类，继承自Node，代表组合节点
class Container(Node):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, node):
        self.children.append(node)

    def draw(self, icon_family, level=0, is_last=False):
        return NotImplemented


# 叶节点类，继承自Node
class Leaf(Node):
    def __init__(self, name):
        super().__init__(name)

    def draw(self, icon_family, level=0, is_last=False):
        return NotImplemented
