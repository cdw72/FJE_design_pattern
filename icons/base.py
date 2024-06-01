from abc import ABC, abstractmethod


# 抽象工厂模式中的抽象产品类
class IconFamily(ABC):
    def __init__(self):
        self.icons = {
            'node': '',
            'leaf': ''
        }

    @abstractmethod
    def get_icons(self):
        return self.icons
