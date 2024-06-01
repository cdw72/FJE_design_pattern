from abc import ABC, abstractmethod


class Node(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def draw(self, icon_family, level=0, is_last=False):
        pass


class Container(Node):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, node):
        self.children.append(node)

    def draw(self, icon_family, level=0, is_last=False):
        return NotImplemented


class Leaf(Node):
    def __init__(self, name):
        super().__init__(name)

    def draw(self, icon_family, level=0, is_last=False):
        return NotImplemented
